#coding=utf-8
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class MetroApp(CMSApp):
    name = _("Metro App")
    urls = ["montecatini_metro.urls"]

apphook_pool.register(MetroApp)
