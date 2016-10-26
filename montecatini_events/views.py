#coding=utf-8
import logging
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import Event
logger = logging.getLogger(__name__)


def event(request, ID=None):
    if ID:
        try:
            current = Event.objects.get(id=ID, published=True)
        except Event.DoesNotExist:
            raise Http404
        except:
            raise Http404
        page_params = {
            'item': current
        }
        template = "events/page.html"
    else:
        all_events = []
        all_titles = []
        cont = 0
        for e in Event.objects.filter(published=True):
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
        template = "events/index.html"
    return render_to_response(template, page_params, context_instance=RequestContext(request))
