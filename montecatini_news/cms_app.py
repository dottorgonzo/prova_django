#coding=utf-8
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
#from .menu import NewsMenu


class NewsApp(CMSApp):
    #menus = [NewsMenu]
    name = _("News App")
    urls = ["montecatini_news.urls"]

apphook_pool.register(NewsApp)
