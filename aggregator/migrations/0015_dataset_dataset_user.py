# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 14:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aggregator', '0014_dataset_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='dataset_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
