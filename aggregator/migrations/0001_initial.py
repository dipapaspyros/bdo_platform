# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 08:37
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('source', models.TextField()),
                ('description', models.TextField()),
                ('references', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128)),
                ('unit', models.CharField(max_length=64)),
                ('min', models.FloatField(blank=True, default=None, null=True)),
                ('max', models.FloatField(blank=True, default=None, null=True)),
                ('step', models.FloatField(blank=True, default=None, null=True)),
                ('axis', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128)),
                ('unit', models.CharField(max_length=64)),
                ('scale_factor', models.FloatField(default=1)),
                ('add_offset', models.FloatField(default=0)),
                ('cell_methods', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('type_of_analysis', models.TextField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variables', to='aggregator.Dataset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dimension',
            name='variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimensions', to='aggregator.Variable'),
        ),
    ]
