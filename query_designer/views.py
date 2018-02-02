# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bson import ObjectId
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from mongo_client import get_mongo_db, MongoResponse


from query_designer.postgres_api import *
from query_designer.postgres_query import *

# from query_designer.mongo_api import *
# from query_designer.mongo_query import *


def index(request):
    return render(request, 'query_designer/index.html', {
        'sidebar_active': 'queries',
    })


def load_query(request, pk):
    q = Query.objects.get(pk=pk)

    return JsonResponse({
        'pk': q.pk,
        'title': q.title,
        'design': q.design,
    })


@csrf_exempt
def save_query(request, pk=None):
    # create or update
    if not pk:
        current_user = request.user
        if current_user.is_authenticated():
            q = Query(user=current_user)
        else:
            q = Query(user=User.objects.get(username='BigDataOcean'))
    else:
        q = Query.objects.get(pk=pk)

    # document
    if 'document' in request.POST:
        try:
            doc = json.loads(request.POST.get('document', ''))
        except ValueError:
            return JsonResponse({'error': 'Invalid query document'}, status=400)

        q.document = doc

    # design
    if 'design' in request.POST:
        try:
            design = json.loads(request.POST.get('design', ''))
        except ValueError:
            return JsonResponse({'error': 'Invalid design'}, status=400)

        q.design = design
    else:
        q.design = None

    # title
    if 'title' in request.POST:
        q.title = request.POST.get('title', 'Untitled query')

    # save
    q.save()

    # return OK response
    return JsonResponse({
        'pk': q.pk,
        'title': q.title,
    })


def get_query_variables(request):
    if 'id' in request.GET:
        id = int(request.GET.get('id'))
        doc = None
        # existing saved query
        if id >= 0:
            # get the query
            q = Query.objects.get(pk=id)
            # get the document
            doc = q.document
        # new query
        else:
            if 'document' in request.GET:
                try:
                    doc = json.loads(request.GET.get('document', ''))
                except ValueError:
                    return JsonResponse({'error': 'Invalid query document'}, status=400)

        # find the query's SELECT variables formatted as: 'variable's column name (title)': 'variable's name'
        variables = dict()
        dimensions = dict()
        for from_clause in doc['from']:
            for col in from_clause['select']:
                if col['type'] == 'VALUE':
                    variables[col['title']] = col['name']
                else:
                    dimensions[col['title']] = col['name']

        result = {'variables': variables, 'dimensions': dimensions}
        # return the found variables
        return HttpResponse(json.dumps(result), content_type="application/json")

    else:
        return JsonResponse({'error': 'Invalid query document'}, status=400)


def load_to_analysis(request):
    current_user = request.user
    if current_user.is_authenticated():
        q = Query(user=current_user)
    else:
        q = Query(user=User.objects.get(username='BigDataOcean'))

    # document
    if 'document' in request.GET:
        try:
            doc = json.loads(request.GET.get('document', ''))
        except ValueError:
            return JsonResponse({'error': 'Invalid query document'}, status=400)

        q.document = doc

    # title
    if 'title' in request.GET:
        q.title = request.GET.get('title', 'Untitled query')

    # return OK response
    return JsonResponse({
        'raw_query': q.raw_query,
        'title': q.title,
    })


def new_template(request):
    return render(request, 'query_designer/new_template.html', {})
