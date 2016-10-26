#coding=utf-8
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class CCNApp(CMSApp):
    name = _("CCN App")
    urls = ["montecatini_ccn.urls"]

apphook_pool.register(CCNApp)
