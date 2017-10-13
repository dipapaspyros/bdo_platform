# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-13 13:20
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_auto_20170823_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobinstance',
            name='base_analysis',
        ),
        migrations.AddField(
            model_name='jobinstance',
            name='analysis_flow',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
    ]
