# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-29 10:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wave_energy_pilot', '0004_wave_energy_converters_period_step'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wave_energy_converters',
            name='owner_id',
        ),
    ]