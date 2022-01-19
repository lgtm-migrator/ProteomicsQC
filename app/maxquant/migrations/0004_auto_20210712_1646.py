# Generated by Django 3.2.3 on 2021-07-12 16:46

from django.db import migrations, models
import main.settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('maxquant', '0003_auto_20210601_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastafile',
            name='fasta_file',
            field=models.FileField(help_text='Fasta file to use with MaxQuant. If this is changed all MaxQuant jobs in this pipeline should be rerun. Note: The link above does not work.', max_length=3000, storage=main.settings.MediaFileSystemStorage(location='/compute'), upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='maxquantexecutable',
            name='filename',
            field=models.FileField(help_text='Upload a zipped MaxQuant file (e.g. MaxQuant_1.6.10.43.zip)', storage=main.settings.MediaFileSystemStorage(location='/compute'), unique=True, upload_to='software/MaxQuant'),
        ),
        migrations.AlterField(
            model_name='maxquantparameter',
            name='mqpar_file',
            field=models.FileField(help_text='mqpar.xml file to use with MaxQuant. If this is changed all MaxQuant jobs in this pipeline should be rerun. Note: The link above does not work.', max_length=3000, storage=main.settings.MediaFileSystemStorage(location='/compute'), upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='maxquantpipeline',
            name='maxquant_executable',
            field=models.FilePathField(blank=True, help_text='If this field is empty the default MaxQuant version (1.6.10.43) will be used. To try a different version go to MaxQuant Executables. If this is changed, all MaxQuant jobs in this pipeline should be rerun.', match='.*MaxQuantCmd.exe', null=True, path='/compute', recursive=True),
        ),
        migrations.AlterField(
            model_name='maxquantpipeline',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, help_text='UID to use the pipeline with the Python API (in the lrg-omics package)', max_length=36),
        ),
    ]
