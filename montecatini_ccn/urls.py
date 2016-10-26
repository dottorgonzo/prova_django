#coding=utf-8
from django.conf.urls import *
from .models import RootCategory

urlpatterns = patterns(
    'montecatini_ccn.views',
    url(r'(?P<rootID>.*)/(?P<categoryID>.*)/(?P<placeID>.*)/$', 'place', name='ccn_place'),
    url(r'(?P<rootID>.*)/(?P<categoryID>.*)/$', 'category', name='ccn_category'),
    url(r'(?P<rootID>.*)/$', 'index', name='ccn_index'),
    url(r'^', 'redirect',),
)
