# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-18 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_builder', '0005_auto_20190218_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardaccessrequest',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
    ]
