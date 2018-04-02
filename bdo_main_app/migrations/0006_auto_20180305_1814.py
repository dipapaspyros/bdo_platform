# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdo_main_app', '0005_auto_20171127_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[(b'dataset', b'Dataset'), (b'analysis', b'Analysis'), (b'dashboard', b'Dashboard')], max_length=32),
        ),
    ]
