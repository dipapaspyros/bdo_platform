# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-21 15:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_builder', '0009_auto_20190221_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardaccessrequest',
            name='response_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dashboardaccessrequest',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 17, 16, 4, 279000)),
        ),
        migrations.AlterField(
            model_name='dashboardaccessrequest',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource', to='dashboard_builder.Dashboard'),
        ),
    ]
