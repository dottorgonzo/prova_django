#coding=utf-8
from django.conf.urls import *

urlpatterns = patterns(
    'montecatini_map.views',
    url(r'^data.json', 'map_view', {'json_response': True}, name='montecatini_map_json'),
    url(r'^', 'map_view', name='montecatini_map'),
)
