# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-23 11:20
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion

from bdo_main_app.lists import SERVICE_TYPES


def get_service_type_by_id(id):
    return [st for st in SERVICE_TYPES if st['id'] == id][0]


def create_default_services(apps, schema_editor):

    from bdo_main_app.models import Service, User

    bdo = User.objects.get_or_create(username='BigDataOcean')[0]

    def create_base_analysis(title, moto='', args=None):
        base_analysis = Service(user=bdo,
                                title=title,
                                service_type='analysis',
                                hidden=True,
                                moto=moto,
                                info={
                                    'extendable': True,
                                    'arguments': args if args else []
                                })

        base_analysis.save()

        return base_analysis

    create_base_analysis('Clustering',
                         'Automatically categorises data into various groups (<em>clusters</em>)')
    create_base_analysis('Regression',
                         'Helps you identify possible correlations between two or more different variables',
                         args=[
                            {'name': 'query', 'type': 'QUERY', 'title': 'Query', },
                            {'name': 'x', 'type': 'COLUMN', 'title': 'Variable X', },
                            {'name': 'y', 'type': 'COLUMN', 'title': 'Variable Y', },
                         ])
    create_base_analysis('Decision tree',
                         'Generates a tree model that will be used for classifying ' +
                         'your data base on a <em>training</em> dataset')
    create_base_analysis('Classification',
                         'Categorises data given that you classify manually some data for <em>training</em>')
    create_base_analysis('Recommendation',
                         'Proposes recommendations based on a training dataset of historical actions')
    create_base_analysis('Association rules',
                         'Generates a set of rules that associate different events with each other')


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=512)),
                ('moto', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('tags_raw', models.TextField(blank=True, default='')),
                ('service_type', models.CharField(choices=[('dataset', 'Dataset'), ('analysis', 'Analysis'), ('analysis', 'Analysis')], max_length=32)),
                ('hidden', models.BooleanField(default=False)),
                ('info', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(create_default_services),
    ]