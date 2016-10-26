#coding=utf-8
import logging
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import Category, Place
logger = logging.getLogger(__name__)


def redirect(request):
    return HttpResponseRedirect(reverse('montecatini_ccn.views.index', None, [1]))


def index(request, rootID):
    all_categories = []
    all_titles = []
    for c in Category.objects.filter(root=rootID):
        try:
            all_titles.append(c.title)
            all_categories.append(c)
        except Exception, ex:
            logger.warning(ex)
    page_params = {
        'categories': all_categories,
        'rootID': int(rootID)
    }
    template = "ccn/index.html"
    return render_to_response(template, page_params, context_instance=RequestContext(request))


def category(request, categoryID, rootID=None):
    try:
        current = Category.objects.get(id=categoryID, root=rootID)
    except Category.DoesNotExist:
        raise Http404
    except Exception, ex:
        logger.warning(ex)
        raise Http404

    all_titles = []
    all_items = []
    for o in Place.objects.filter(category=current).order_by('-premium'):
        try:
            all_titles.append(o.title)
            all_items.append(o)
        except Exception, ex:
            logger.warning(ex)

    page_params = {
        'category': current,
        'rootID': current.root,
        'places': all_items,
        'title': current.title,
    }
    template = "ccn/category.html"
    return render_to_response(template, page_params, context_instance=RequestContext(request))


def place(request, categoryID, placeID, rootID=None):
    try:
        category = Category.objects.get(id=categoryID, root=rootID)
    except Category.DoesNotExist:
        raise Http404
    except Exception, ex:
        logger.warning(ex)
        raise Http404

    try:
        current = Place.objects.get(id=placeID, category=category)
    except Place.DoesNotExist:
        raise Http404
    except Exception, ex:
        logger.warning(ex)
        raise Http404

    page_params = {
        'category': category,
        'place': current,
        'rootID': category.root,
        'title': current.title,
    }
    template = "ccn/place.html"
    return render_to_response(template, page_params, context_instance=RequestContext(request))
