#coding=utf-8
from django.conf.urls import *

urlpatterns = patterns(
    'montecatini_metro.views',
    url(r'(?P<slug>.*)/$', 'line', name='metro_line'),
    url(r'^', 'redirect',),
)
