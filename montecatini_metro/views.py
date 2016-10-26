#coding=utf-8
import logging
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import PointOfInterest, Lines, SliderPicture
logger = logging.getLogger(__name__)


def redirect(request):
    return HttpResponseRedirect(reverse('montecatini_metro.views.line', None, [Lines.RED]))


def line(request, slug):
    if slug == Lines.RED:
        classname = "linearossa"
    elif slug == Lines.YELLOW:
        classname = "lineagialla"
    elif slug == Lines.GREEN:
        classname = "lineaverde"
    elif slug == Lines.BLUE:
        classname = "lineablu"
    else:
        raise Http404

    all_titles = []
    all_pois = []
    all_latlng = []
    for p in PointOfInterest.objects.filter(line=slug):
        try:
            all_titles.append(p.title)
            all_pois.append(p)
            if p.latitude != 0 and p.longitude != 0:
                all_latlng.append(p)
        except Exception, ex:
            logger.exception(ex)

    page_params = {
        'slug': slug,
        'class': classname,
        'pois': all_pois,
        'pois_latlng': all_latlng,
        'slider': SliderPicture.objects.filter(area=slug),
    }
    template = "metro/linea.html"
    return render_to_response(template, page_params, context_instance=RequestContext(request))
