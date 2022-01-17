# from dash.html.Pre import Pre
import pandas as pd
import numpy as np

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import dash_table as dt

from plotly import express as px

from dash_tabulator import DashTabulator

from lrg_omics.proteomics import ProteomicsQC

try:
    from . import tools as T
except:
    import tools as T


layout = html.Div(
    [
        html.H1("Anomaly detection"),
        html.Button("Run isolation forest", id="anomaly-btn", className="btn"),
        dcc.Loading(
            [dcc.Graph(id="anomaly-figure")],
        ),
        dcc.Markdown("Anormal feature values have lower z-values."),
    ]
)


def callbacks(app):
    @app.callback(
        Output("anomaly-figure", "figure"),
        Input("anomaly-btn", "n_clicks"),
        State("qc-table", "data"),
        State("project", "value"),
        State("pipeline", "value"),
    )
    def run_anomaly_detection(n_clicks, data, project, pipeline):
        if n_clicks is None:
            raise PreventUpdate

        pqc = ProteomicsQC(
            host="http://localhost:8000",
            project_slug=project,
            pipeline_slug=pipeline,
        )

        qc_data = pqc.get_qc_data(data_range=None).set_index("RawFile")

        predictions, df_shap = T.detect_anomalies(qc_data)

        fig = T.px_heatmap(
            df_shap.T,
            layout_kws=dict(
                title="Anomaly feature score (shapley values)", height=1200
            ),
        )

        files_to_flag = predictions[predictions.Anomaly==1].index.to_list()
        files_to_unflag = predictions[predictions.Anomaly==0].index.to_list()
        pqc.flag(files_to_flag)
        pqc.unflag(files_to_unflag)

        return fig
