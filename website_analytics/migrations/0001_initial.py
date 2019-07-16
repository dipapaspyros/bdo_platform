# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-16 13:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visualizer', '0011_visualization_data_source'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service_builder', '0024_auto_20190716_1627'),
        ('dashboard_builder', '0014_auto_20190716_1627'),
        ('aggregator', '0041_auto_20190716_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueDashboardViewsView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboard_id', models.IntegerField(default=1)),
                ('count', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'unique_dashboard_views_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UniqueDatasetPreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_id', models.IntegerField(default=1)),
                ('count', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'unique_dataset_preview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UniqueServiceUsesView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField(default=1)),
                ('count', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'unique_service_uses_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BDO_Plan',
            fields=[
                ('plan_name', models.TextField(primary_key=True, serialize=False)),
                ('plan_title', models.TextField(default='Untitled Plan')),
                ('query_limit', models.IntegerField(default=120, null=True)),
                ('price', models.FloatField(default=0, null=True)),
                ('access_to_beta_services', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DashboardDisplays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dash_display_count', models.IntegerField(default=1)),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dashboard_displays_dashboard', to='dashboard_builder.Dashboard')),
            ],
        ),
        migrations.CreateModel(
            name='DashboardUniqueViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dash_display_count', models.IntegerField(default=1)),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dashboard_unique_views_dashboard', to='dashboard_builder.Dashboard')),
                ('dashboard_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dashboard_unique_views_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DatasetCombined',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combination_count', models.IntegerField(default=1)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dataset_combined_dataset', to='aggregator.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='DatasetExplored',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exploration_count', models.IntegerField(default=1)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dataset_explored_dataset', to='aggregator.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='DatasetPageViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview_count', models.IntegerField(default=1)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dataset_page_views_dataset', to='aggregator.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='DatasetUniqueViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview_count', models.IntegerField(default=1)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dataset_unique_views_dataset', to='aggregator.Dataset')),
                ('dataset_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dataset_unique_views_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DatasetUseInService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_count', models.IntegerField(default=1)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dataset_use_in_service_dataset', to='aggregator.Dataset')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dataset_use_in_service_service', to='service_builder.Service')),
            ],
        ),
        migrations.CreateModel(
            name='DatasetUseInVisualisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viz_use_count', models.IntegerField(default=1)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_dataset_use_in_visualisation_dataset', to='aggregator.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='MareProtectionService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scenario', models.IntegerField(default=1)),
                ('simulation_length', models.IntegerField(default=24)),
                ('time_interval', models.IntegerField(default=2)),
                ('ocean_circulation_model', models.CharField(default='Poseidon High Resolution Aegean Model', max_length=100)),
                ('wave_model', models.CharField(default='Poseidon WAM Cycle 4 for the Aegean', max_length=100)),
                ('natura_layer', models.BooleanField(default=False)),
                ('ais_layer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_runs', models.IntegerField(default=1)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_per_user_service', to='service_builder.Service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_per_user_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_use_count', models.IntegerField(default=1)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_service_use_service', to='service_builder.Service')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_use_count', models.IntegerField(default=1)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_service_users_service', to='service_builder.Service')),
                ('service_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_service_users_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('date_end', models.DateTimeField(default=datetime.datetime(2019, 8, 15, 16, 27, 30, 138000))),
                ('active', models.BooleanField(default=True)),
                ('auto_renewal', models.BooleanField(default=True)),
                ('query_count', models.IntegerField(default=0)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_plan', to='website_analytics.BDO_Plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VisualisationTypeUses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viz_use_count', models.IntegerField(default=1)),
                ('visualisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_visualisation_type_uses_visualisation', to='visualizer.Visualization')),
            ],
        ),
        migrations.CreateModel(
            name='WaveEnergyResourceAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_nester_statistics_dataset', to='aggregator.Dataset')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_nester_statistics_service', to='service_builder.Service')),
            ],
        ),
    ]
