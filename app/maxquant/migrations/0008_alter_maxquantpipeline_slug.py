# Generated by Django 3.2.5 on 2021-08-12 18:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('maxquant', '0007_alter_maxquantpipeline_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maxquantpipeline',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, max_length=500),
        ),
    ]
