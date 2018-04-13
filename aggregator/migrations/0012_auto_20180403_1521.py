# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 12:21
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0011_dataset_stored_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='table_name',
            field=models.CharField(default='table', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimension',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='references',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='stored_at',
            field=models.CharField(choices=[(b'LOCAL_POSTGRES', b'Local PostgreSQL instance'), (b'UBITECH_POSTGRES', b"UBITECH's PostgreSQL instance at http://212.101.173.34"), (b'UBITECH_SOLR', b'Solr instance at http://212.101.173.50:8983')], default=b'LOCAL_POSTGRES', max_length=32),
        ),
    ]