# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db.models import *


class Service(Model):
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    # service creator
    user = ForeignKey(User)
    title = CharField(max_length=512)
    private = BooleanField(default=False)
    published = BooleanField(default=False)

    notebook_id = CharField(max_length=100)
    arguments_paragraph_id = CharField(max_length=100, null=True)

    queries = JSONField(default={}, null=True, blank=True)
    arguments = JSONField(default={}, null=True)

    output_html = TextField(null=True)
    output_css = TextField(null=True)
    output_js = TextField(null=True)

    description = CharField(blank=True,max_length=512,null=True,default=None)
    price = CharField(max_length=50,default='free')
    imageurl = URLField(blank=True,null=True, default=None)


class ServiceTemplate(Model):
    html = TextField()
    css = TextField()
    js = TextField()


class ServiceInstance(Model):
    service = ForeignKey(Service)
    user = ForeignKey(User)
    time = DateTimeField()
    arguments = JSONField(null=True, blank=True, default=None)
    notebook_id = CharField(null=True, max_length=100)
    livy_session = IntegerField(null=True)
    status = CharField(null=True, default='', max_length=100)
    output_page = CharField(null=True, default='', max_length=100)
    dataframe_visualizations = JSONField(null=True, blank=True, default=None)
    result = JSONField(null=True, blank=True, default=None)
