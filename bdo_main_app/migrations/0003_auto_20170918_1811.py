# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-18 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdo_main_app', '0002_service_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='job_name',
        ),
    ]