#coding=utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = i18n_patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^ccn/', include('montecatini_ccn.urls')),
    url(r'^events/', include('montecatini_events.urls')),
    url(r'^map/', include('montecatini_map.urls')),
    url(r'^metro/', include('montecatini_metro.urls')),
    url(r'^news/', include('montecatini_news.urls')),
    url(r'^', include('cms.urls')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns(
        '',
        url(r'^rosetta/', include('rosetta.urls')),
    )

urlpatterns += patterns(
    '',
    url(r'^favicon.ico$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'path': 'icone/favicon.ico'}),
    url(r'^favicon.png$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'path': 'icone/favicon.png'}),
    url(r'^apple-touch-iphone4$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'path': 'icone/apple-touch-iphone4'}),
    url(r'^apple-touch-ipad.png$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'path': 'icone/apple-touch-ipad.png'}),
    url(r'^apple-touch-ipad-retina.png$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'path': 'icone/apple-touch-ipad-retina.png'}),
)

if settings.DEBUG:
    urlpatterns = patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
else:
    urlpatterns = patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    ) + urlpatterns
