# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-02 13:00
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('source', models.TextField()),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=999)),
                ('references', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None)),
                ('stored_at', models.CharField(choices=[(b'LOCAL_POSTGRES', b'Local PostgreSQL instance'), (b'UBITECH_POSTGRES', b"UBITECH's PostgreSQL instance at http://212.101.173.21"), (b'UBITECH_PRESTO', b"UBITECH's PRESTO instance"), (b'UBITECH_SOLR', b'Solr instance at http://212.101.173.50:8983')], default=b'LOCAL_POSTGRES', max_length=32)),
                ('table_name', models.CharField(max_length=200)),
                ('private', models.BooleanField(default=False)),
                ('spatialEast', models.CharField(max_length=200, null=True)),
                ('spatialSouth', models.CharField(max_length=200, null=True)),
                ('spatialNorth', models.CharField(max_length=200, null=True)),
                ('spatialWest', models.CharField(max_length=200, null=True)),
                ('temporalCoverageBegin', models.DateTimeField(null=True)),
                ('temporalCoverageEnd', models.DateTimeField(null=True)),
                ('license', models.CharField(max_length=200, null=True)),
                ('observations', models.CharField(max_length=200, null=True)),
                ('publisher', models.TextField()),
                ('category', models.CharField(max_length=200, null=True)),
                ('image_uri', models.TextField(default=b'/static/img/logo.png')),
                ('sample_rows', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('number_of_rows', models.CharField(max_length=200, null=True)),
                ('size_in_gb', models.FloatField(null=True)),
                ('update_frequency', models.CharField(default=b'-', max_length=200)),
                ('last_updated', models.DateTimeField(null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('hascoverage_img', models.BooleanField(default=False)),
                ('arguments', django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DatasetAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('valid', models.BooleanField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregator.Dataset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DatasetAccessRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(b'open', b'open'), (b'accepted', b'accepted'), (b'rejected', b'rejected')], default=b'open', max_length=20)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2019, 7, 2, 16, 0, 44, 312000))),
                ('response_date', models.DateTimeField(null=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource', to='aggregator.Dataset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('unit', models.CharField(max_length=256)),
                ('description', models.TextField(null=True)),
                ('sameAs', models.CharField(max_length=256, null=True)),
                ('dataType', models.CharField(max_length=256, null=True)),
                ('original_column_name', models.CharField(max_length=256, null=True)),
                ('min', models.DecimalField(blank=True, decimal_places=50, default=None, max_digits=100, null=True)),
                ('max', models.DecimalField(blank=True, decimal_places=50, default=None, max_digits=100, null=True)),
                ('step', models.DecimalField(blank=True, decimal_places=50, default=None, max_digits=100, null=True)),
                ('axis', models.TextField(blank=True, default=None, null=True)),
                ('non_filterable', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='JoinOfDatasets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_name', models.CharField(max_length=100)),
                ('dataset_first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first', to='aggregator.Dataset')),
                ('dataset_second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second', to='aggregator.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('unit', models.CharField(max_length=256)),
                ('description', models.TextField(null=True)),
                ('sameAs', models.CharField(max_length=256, null=True)),
                ('dataType', models.CharField(max_length=256, null=True)),
                ('original_column_name', models.CharField(max_length=256, null=True)),
                ('scale_factor', models.FloatField(default=1)),
                ('add_offset', models.FloatField(default=0)),
                ('cell_methods', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None)),
                ('type_of_analysis', models.TextField(blank=True, default=None, null=True)),
                ('distribution', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, default=None, null=True, size=7)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variables', to='aggregator.Dataset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vessel_Identifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=200)),
                ('values_list', django.contrib.postgres.fields.jsonb.JSONField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vessel_identifiers', to='aggregator.Dataset')),
            ],
        ),
        migrations.AddField(
            model_name='dimension',
            name='variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimensions', to='aggregator.Variable'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='access_list',
            field=models.ManyToManyField(through='aggregator.DatasetAccess', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dataset',
            name='joined_with_dataset',
            field=models.ManyToManyField(related_name='joined_to', through='aggregator.JoinOfDatasets', to='aggregator.Dataset'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to='aggregator.Organization'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dataset_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
