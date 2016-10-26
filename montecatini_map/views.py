#coding=utf-8
import json
import logging
import math
import operator
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import ugettext_lazy as _
from montecatini_ccn.models import Place, RootCategory
from montecatini_metro.models import PointOfInterest, Lines
logger = logging.getLogger(__name__)


def distance(origin, destination):
    """
    http://www.platoscave.net/blog/2009/oct/5/calculate-distance-latitude-longitude-python/
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d


def map_view(request, json_response=False):
    if json_response:
        pois = []
        origin_point = (float(request.GET.get('latitude', 43.880633)), float(request.GET.get('longitude', 10.7720853)))

        for p in PointOfInterest.objects.exclude(latitude=0, longitude=0):
            try:
                if p.line == Lines.RED:
                    map_type = "linearossa"
                elif p.line == Lines.GREEN:
                    map_type = "lineaverde"
                elif p.line == Lines.YELLOW:
                    map_type = "lineagialla"
                elif p.line == Lines.BLUE:
                    map_type = "lineablu"
                else:
                    map_type = "metro"

                distance_calculated = -1
                if p.latitude and p.longitude:
                    distance_calculated = int(distance((p.latitude, p.longitude), origin_point) * 1000)

                pois.append({
                    'type': map_type,
                    'latitude': p.latitude,
                    'longitude': p.longitude,
                    'distance': distance_calculated,
                    'title': p.title,
                    'url': p.get_absolute_url(),
                    'id': "metro_%s" % p.id
                })
            except Exception, ex:
                logger.warning(ex)

        for p in Place.objects.exclude(latitude=0, longitude=0):
            try:
                if p.category.root == RootCategory.SHOPPING:
                    map_type = "shopping"
                elif p.category.root == RootCategory.TEMPO_LIBERO:
                    map_type = "tempolibero"
                elif p.category.root == RootCategory.BERE_E_MANGIARE:
                    map_type = "mangiare"
                elif p.category.root == RootCategory.DORMIRE:
                    map_type = "dormire"
                elif p.category.root == RootCategory.SERVIZI:
                    map_type = "servizi"
                else:
                    map_type = "ccn"

                distance_calculated = -1
                if p.latitude and p.longitude:
                    distance_calculated = int(distance((p.latitude, p.longitude), origin_point) * 1000)

                pois.append({
                    'type': map_type,
                    'latitude': p.latitude,
                    'longitude': p.longitude,
                    'distance': distance_calculated,
                    'title': p.title,
                    'url': p.get_absolute_url(),
                    'id': "ccn_%s" % p.id
                })
            except Exception, ex:
                logger.warning(ex)

        pois = sorted(pois, key=operator.itemgetter("distance"))

        response = HttpResponse(mimetype='application/json')
        response.write(json.dumps(pois))
        return response
    else:
        types = [
            ('linearossa',  _('Il Vialone dei Bagni')),
            ('lineagialla', _('Montecatini Alto')),
            ('lineaverde', _('Il 900')),
            ('lineablu', _('Arte e Cultura')),
            ('shopping', _('Shopping')),
            ('tempolibero', _('Free Time')),
            ('mangiare', _('Food and Drink')),
            ('dormire', _('Lodging')),
            ('servizi', _('Services')),
        ]

        page_params = {
            'pois': [],
            'types': types,
        }
        template = "map/map.html"
        return render_to_response(template, page_params, context_instance=RequestContext(request))
