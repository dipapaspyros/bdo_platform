# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 12:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequests',
            name='deadline',
            field=models.DateField(default=datetime.date(2018, 4, 3)),
        ),
    ]