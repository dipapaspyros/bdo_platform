# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-18 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdo_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='business_role',
            field=models.TextField(blank=True, default=''),
        ),
    ]
