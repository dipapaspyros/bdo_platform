# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 14:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query_designer', '0012_query_dataset_query'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='dataset_query',
        ),
    ]