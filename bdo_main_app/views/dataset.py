# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta
from django.shortcuts import render
from django.utils.timezone import now

from bdo_main_app.models import SERVICES


def dataset(request, slug):
    return render(request, 'services/datasets/index.html', {
        'sidebar_active': 'products',
        'dataset': SERVICES[0],
    })




