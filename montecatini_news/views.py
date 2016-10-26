#coding=utf-8
import logging
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import News
logger = logging.getLogger(__name__)


def news(request, ID=None):
    if ID:
        try:
            current = News.objects.get(id=ID, published=True)
        except News.DoesNotExist:
            raise Http404
        except:
            raise Http404
        page_params = {
            'item': current
        }
        template = "news/page.html"
    else:
        all_events = []
        all_titles = []
        cont = 0
        for e in News.objects.filter(published=True):
            try:
                all_titles.append(e.title)
                all_events.append(e)
                cont += 1
                if cont > 20:
                    break
            except:
                pass
        page_params = {
            'items': all_events
        }
        template = "news/index.html"
    return render_to_response(template, page_params, context_instance=RequestContext(request))
