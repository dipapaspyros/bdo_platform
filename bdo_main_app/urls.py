from django.conf.urls import url

import bdo_main_app.views as views
import service_builder.views as sb_views

urlpatterns = [
    # home & signup
    url('^$', views.home, name='home'),
    # Terms of Usage
    url('^terms/$', views.terms, name='terms'),
    url('^plans/$', views.plans, name='plans'),
    url('^documentation/$', views.documentation, name='documentation'),
    url('^bdo/$', views.dataset_search, name='bdo'),
    url('^search/$', views.search, name='search'),
    url('^exploretools/$', views.exploretools, name='exploretools'),

    url('^analytics-environment/$', views.search, name='search'),


    # datasets
    url('^datasets/(?P<dataset_id>[\w-]+)/$', views.dataset, name='dataset-details'),

    # on demand
    # url('^on-demand/$', views.on_demand_search, name='on-demand'),
    # url('^on-demand/create/$', views.on_demand_create, name='on-demand-create'),

    # service and dashboards
    url('^services/$', views.services, name='services'), #Service Marketplace
    url('^services/dashboard/(?P<pk>\d+)/$', views.view_dashboard, name='view_dashboard'),
    url('^services/service/(?P<pk>\d+)/$', sb_views.load_service, name='load_service'),
    url('^services/list/$', sb_views.list_services, name='list_services'),
    url('^services/(?P<pk>\d+)/arguments/$', sb_views.list_service_args, name='list_service_args'),
    url('^services/(?P<pk>\d+)/status/$', sb_views.get_service_inst_status, name='get_service_inst_status'),

    url('^pilot/wave-energy/$', views.load_nester_service, name='wave-energy-pilot'),
    url('^pilot/anomaly-detection/$', views.load_xmile_service, name='wave-energy-pilot'),
    url('^pilot/oil-spill-simulation/$', views.load_hcmr_service, name='wave-energy-pilot'),
    url('^pilot/fault-prediction-anek/$', views.load_anek_service, name='wave-energy-pilot'),
    url('^pilot/fault-prediction-fnk/$', views.load_fnk_service, name='wave-energy-pilot'),
]
