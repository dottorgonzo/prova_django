import datetime
from cms.models import Page
from django import template
from django.template.loader_tags import register


class GetAllLocations(template.Node):
    def render(self, context):

        pois = []

        pages = Page.objects.filter(
            published=True,
            login_required=False,
            publisher_state=0,
            publisher_is_draft=False,
            #publisher_public=None,

        )
        for page in pages:
            for placeholder in page.placeholders.all():
                if placeholder.slot == 'details_geolocation':
                    for plugin in placeholder.get_plugins():
                        if plugin.get_plugin_instance()[0]:
                            pois.append({
                                'instance_id': plugin.get_plugin_instance()[0].id,
                                'title': page.get_title(),
                                'latitude': plugin.get_plugin_instance()[0].latitude,
                                'longitude': plugin.get_plugin_instance()[0].longitude,
                                'url': page.get_absolute_url(),
                            })

        context['pois'] = pois
        return ''


@register.tag(name="get_all_locations")
def get_all_locations(parser, token):
    return GetAllLocations()
