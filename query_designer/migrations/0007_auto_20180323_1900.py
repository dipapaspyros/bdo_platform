# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 17:00
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('query_designer', '0006_auto_20180202_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Untitled query')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('generated_by', models.CharField(choices=[('CUSTOM', 'Custom query'), ('QDv1', 'Query Designer (old)'), ('QDv2', 'Query Designer (new)')], max_length=32)),
                ('document', django.contrib.postgres.fields.jsonb.JSONField()),
                ('design', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
                ('v2_fields', models.TextField(blank=True, default=None, editable=False, null=True)),
                ('v2_filters', models.TextField(blank=True, default=None, editable=False, null=True)),
                ('count', models.IntegerField(blank=True, default=None, null=True)),
                ('headers', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='formula',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='query',
            name='count',
        ),
        migrations.RemoveField(
            model_name='query',
            name='created',
        ),
        migrations.RemoveField(
            model_name='query',
            name='design',
        ),
        migrations.RemoveField(
            model_name='query',
            name='document',
        ),
        migrations.RemoveField(
            model_name='query',
            name='generated_by',
        ),
        migrations.RemoveField(
            model_name='query',
            name='headers',
        ),
        migrations.RemoveField(
            model_name='query',
            name='id',
        ),
        migrations.RemoveField(
            model_name='query',
            name='title',
        ),
        migrations.RemoveField(
            model_name='query',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='query',
            name='user',
        ),
        migrations.RemoveField(
            model_name='query',
            name='v2_fields',
        ),
        migrations.RemoveField(
            model_name='query',
            name='v2_filters',
        ),
        migrations.CreateModel(
            name='TempQuery',
            fields=[
                ('abstractquery_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='query_designer.AbstractQuery')),
            ],
            bases=('query_designer.abstractquery',),
        ),
        migrations.DeleteModel(
            name='Formula',
        ),
        migrations.AddField(
            model_name='abstractquery',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='query',
            name='abstractquery_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='query_designer.AbstractQuery'),
            preserve_default=False,
        ),
    ]