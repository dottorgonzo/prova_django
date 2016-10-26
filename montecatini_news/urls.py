#coding=utf-8
from django.conf.urls import *

urlpatterns = patterns(
    'montecatini_news.views',
    url(r'(?P<ID>.*)/$', 'news', name="montecatini_news"),
    url(r'^', 'news', name="montecatini_news"),
)
