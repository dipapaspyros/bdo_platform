# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 11:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service_builder', '0016_service_through_livy'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='service',
            name='user',
            field=models.CharField(max_length=512),
        ),
    ]