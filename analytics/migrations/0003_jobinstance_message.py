# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-22 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20170622_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinstance',
            name='message',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]