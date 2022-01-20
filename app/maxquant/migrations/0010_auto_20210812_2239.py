# Generated by Django 3.2.5 on 2021-08-12 22:39

from django.db import migrations, models
import main.settings


class Migration(migrations.Migration):

    dependencies = [
        ('maxquant', '0009_alter_maxquantexecutable_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastafile',
            name='fasta_file',
            field=models.FileField(help_text='Fasta file to use with MaxQuant. If this is changed all MaxQuant jobs in this pipeline should be rerun. Note: The link above does not work.', max_length=1000, storage=main.settings.MediaFileSystemStorage(location='/compute'), upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='maxquantparameter',
            name='mqpar_file',
            field=models.FileField(help_text='mqpar.xml file to use with MaxQuant. If this is changed all MaxQuant jobs in this pipeline should be rerun. Note: The link above does not work.', max_length=1000, storage=main.settings.MediaFileSystemStorage(location='/compute'), upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='maxquantpipeline',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]