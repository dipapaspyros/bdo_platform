# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-23 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def remove_existing_jobs(apps, schema_editor):

    from analytics.models import JobInstance

    JobInstance.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('bdo_main_app', '0001_initial'),
        ('analytics', '0003_jobinstance_message'),
    ]

    operations = [
        migrations.RunPython(remove_existing_jobs),
        migrations.RemoveField(
            model_name='jobinstance',
            name='service_id',
        ),
        migrations.AddField(
            model_name='jobinstance',
            name='base_analysis',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bdo_main_app.Service'),
        ),
    ]
