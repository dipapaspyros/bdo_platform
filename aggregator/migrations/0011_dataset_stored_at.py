# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-12 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0010_dimension_non_filterable'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='stored_at',
            field=models.CharField(choices=[(b'LOCAL_POSTGRES', b'Local PostgreSQL instance'), (b'UBITECH_SOLR', b'Solr instance at http://212.101.173.50:8983')], default=b'LOCAL_POSTGRES', max_length=32),
        ),
    ]
