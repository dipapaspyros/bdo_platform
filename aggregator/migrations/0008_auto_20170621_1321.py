# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 10:21
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0007_auto_20170515_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataset',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='dimension',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='variable',
            name='distribution',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, default=None, null=True, size=7),
        ),
    ]