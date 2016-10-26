#coding=utf-8
import urllib
from cms.admin.placeholderadmin import PlaceholderAdmin
from django.contrib.admin import site, TabularInline
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from hvad.admin import TranslatableAdmin, TranslatableTabularInline
from .models import PointOfInterest, Picture, SubContent, SliderPicture
from ordered_model.admin import OrderedModelAdmin


class PictureInlineAdmin(TabularInline):
    model = Picture
    max_num = 10
    extra = 3


class SubContentInlineAdmin(TranslatableTabularInline):
    model = SubContent
    extra = 3


class PointOfInterestAdmin(OrderedModelAdmin, TranslatableAdmin, PlaceholderAdmin):
    inlines = [SubContentInlineAdmin, PictureInlineAdmin]
    list_display = ('line', 'get_title', 'latitude', 'longitude', 'move_up_down_links', 'all_translations', 'qr_code')
    list_display_links = ('get_title', )
    list_filter = ('line', )

    def get_title(self, obj):
        return obj.safe_translation_getter('title', unicode(obj.pk))
    get_title.short_description = _('title')

    def qr_code(self, obj):
        data = "http://montecatiniterme.ivirgilius.com%s" % obj.get_absolute_url()
        small = "http://api.qrserver.com/v1/create-qr-code/?%s" % urllib.urlencode({'data': data, 'size': "50x50"})
        big = "http://api.qrserver.com/v1/create-qr-code/?%s" % urllib.urlencode({'data': data, 'size': "1000x1000"})
        return "<a href='%s'><img src='%s' width='50' height='50' /></a>" % (big, small)
    qr_code.allow_tags = True

site.register(PointOfInterest, PointOfInterestAdmin)


class SliderPictureAdmin(OrderedModelAdmin):
    list_display = ('area', 'image', 'move_up_down_links', )
    list_display_links = ('image', )
    list_filter = ('area', )

site.register(SliderPicture, SliderPictureAdmin)
site.unregister(Site)
