# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-02 13:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import s3direct.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_raw', s3direct.fields.S3DirectField(blank=True, default=None, null=True)),
                ('first_name', models.TextField(blank=True, default='')),
                ('last_name', models.TextField(blank=True, default='')),
                ('organization', models.TextField(blank=True, default='')),
                ('user_type', models.CharField(blank=True, choices=[('', ''), ('DATA_ANALYST', 'Data analyst'), ('BUSINESS_USER', 'Business user'), ('RESEARCHER', 'Researcher'), ('SERVICE_DEVELOPER', 'Service developer')], default='', max_length=32)),
                ('business_role', models.TextField(blank=True, default='')),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('external_url', models.URLField(blank=True, default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
