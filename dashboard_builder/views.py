from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from query_designer.models import Query
from visualizer.models import Visualization
from dashboard_builder.models import Dashboard
from aggregator.models import *

from . import forms

import json
import collections
def build_dynamic_dashboard(request):

    if request.method == 'GET':
        user = request.user
        if request.user.is_authenticated():
            saved_queries = Query.objects.filter(user=user).exclude(document__from=[])

        else:
            saved_queries = []

        variables_list = []
        dimensions_list = []
        var_list = Variable.objects.all()
        dim_list = Dimension.objects.all()
        for el in var_list:
            if not (el.name in variables_list):
                variables_list.append(el.name.encode('ascii'))
        for el in dim_list:
            if not (el.name in dimensions_list):
                dimensions_list.append(el.name.encode('ascii'))

        num_of_dashboards = Dashboard.objects.count()
        toCreate = request.GET.get('toCreate', 'None')
        form_class = forms.CkEditorForm
        return render(request, 'dashboard_builder/dashboardbuilder3.html', {
            'dashboard_title': num_of_dashboards+1,
            'sidebar_active': 'products',
            'saved_queries': saved_queries,
            'available_viz': Visualization.objects.filter(hidden=False).order_by('-type','-title'),
            'form_class': form_class,
            # 'components': Visualization.objects.all().order_by('order'),
            'form': form_class,
            'toCreate': toCreate,
            'variables_list': variables_list,
            'dimensions_list': dimensions_list,
            # 'datasets_of_queries_lists': datasets,
        })
    return None

def convert_unicode_json(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert_unicode_json, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert_unicode_json, data))
    else:
        return data

def edit_dashboard(request, pk=None):
    if request.method == 'GET':
        user = request.user
        if request.user.is_authenticated():
            saved_queries = Query.objects.filter(user=user).exclude(document__from=[])
        else:
            saved_queries = []
        dashboard = Dashboard.objects.get(pk=pk)
        try:
            if dashboard.user_id != user.id:
                raise PermissionDenied
        except:
            return HttpResponseForbidden()

        variables_list = []
        dimensions_list = []
        var_list = Variable.objects.all()
        dim_list = Dimension.objects.all()
        for el in var_list:
            if not (el.name in variables_list):
                variables_list.append(el.name.encode('ascii'))
        for el in dim_list:
            if not (el.name in dimensions_list):
                dimensions_list.append(el.name.encode('ascii'))
        toCreate = "None"
        form_class = forms.CkEditorForm
        dashboard.viz_components = convert_unicode_json(dashboard.viz_components)
        print dashboard.viz_components
        return render(request, 'dashboard_builder/dashboard_editor_new.html', {
            'dashboard': dashboard,
            'dashboard_json': json.dumps(dashboard.viz_components),
            'dashboard_pk': pk,
            'dashboard_title': dashboard.title,
            'sidebar_active': 'products',
            'saved_queries': saved_queries,
            'available_viz': Visualization.objects.filter(hidden=False).order_by('-type', '-title'),
            'form': form_class,
            'toCreate': toCreate,
            'variables_list': variables_list,
            'dimensions_list': dimensions_list,
        })
    return None

def get_visualization_form_fields(request):
    viz_id = request.GET.get('id')
    order = request.GET.get('order')
    visualization = Visualization.objects.get(pk=viz_id)
    html = render_to_string('dashboard_builder/config-visualization-form-fields.html', {'order': order,
                                                                                        'viz_id': viz_id,
                                                                                        'info': visualization.info,
                                                                                        'action': visualization.view_name})
    return HttpResponse(html)


def get_visualization_form_fields_df(request):
    viz_id = request.GET.get('id')
    order = request.GET.get('order')
    visualization = Visualization.objects.get(pk=viz_id)
    html = render_to_string('dashboard_builder/config-visualization-form-fields-df.html', {'order': order,
                                                                                        'viz_id': viz_id,
                                                                                        'info': visualization.info,
                                                                                        'action': visualization.view_name})
    return HttpResponse(html)


def save_dashboard(request, pk=None):
    # create or update
    if not pk:
        user = request.user
        if user.is_authenticated():
            dashboard = Dashboard(user=user)
        else:
            dashboard = Dashboard(user=User.objects.get(username='BigDataOcean'))

    else:
        dashboard = Dashboard.objects.get(pk=pk)

    dashboard.title = 'BDO Dashboard'
    print request.POST
    dashboard_data = request.POST.dict()
    for order in dashboard_data.keys():
        dashboard_data = json.loads(order)

    print "We are now printing dashboard data"
    print dashboard_data
    print "end of data"
    title = dashboard_data.pop('title', None)
    private = dashboard_data.pop('private', None)

    for order in dashboard_data.keys():
        print order
        print dashboard_data[order]
    dashboard.viz_components = dashboard_data
    dashboard.title = title
    dashboard.private = private
    print dashboard.title

    dashboard.save()

    return JsonResponse({
        'pk': dashboard.pk,
    })


def delete_dashboard(request, pk=None):
    user = request.user
    try:
        dashboard = Dashboard.objects.get(pk=pk)
        try:
            if dashboard.user_id != user.id:
                raise PermissionDenied
        except:
            return HttpResponseForbidden()

        dashboard.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('/bdo')
