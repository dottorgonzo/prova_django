#coding=utf-8
from django.conf.urls import *

urlpatterns = patterns(
    'montecatini_events.views',
    url(r'(?P<ID>.*)/$', 'event', name="montecatini_events"),
    url(r'^', 'event', name="montecatini_events"),
)
