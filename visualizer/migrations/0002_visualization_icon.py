# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-15 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visualization',
            name='icon',
            field=models.ImageField(default='visualizaer/img/default-img.jpg', upload_to='visualizaer/img/'),
        ),
    ]