#coding=utf-8
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
#from .menu import EventsMenu


class EventApp(CMSApp):
    #menus = [EventsMenu]
    name = _("Events App")
    urls = ["montecatini_events.urls"]

apphook_pool.register(EventApp)
