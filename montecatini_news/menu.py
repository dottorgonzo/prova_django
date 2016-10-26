#coding=utf-8
from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from .models import News


class NewsMenu(CMSAttachMenu):
    name = _("News Menu")

    def get_nodes(self, request):
        nodes = []
        for item in News.objects.filter(published=True):
            node = NavigationNode(
                item.__unicode__,
                reverse('montecatini_news.views.news', args=(item.pk,)),
                item.pk
            )
            nodes.append(node)
        return nodes

#menu_pool.register_menu(NewsMenu)
