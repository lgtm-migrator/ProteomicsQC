# Generated by Django 3.2 on 2021-05-05 01:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=36),
        ),
    ]
