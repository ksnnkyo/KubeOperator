# Generated by Django 2.1.2 on 2019-09-23 07:10

import common.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0017_auto_20190919_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='configs',
            field=common.models.JsonDictTextField(default={}),
        ),
    ]