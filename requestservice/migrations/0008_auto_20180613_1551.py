# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-13 12:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestservice', '0007_auto_20180513_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequests',
            name='deadline',
            field=models.DateField(default=datetime.date(2018, 6, 13)),
        ),
    ]
