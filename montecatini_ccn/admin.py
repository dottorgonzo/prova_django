#coding=utf-8
import urllib
from django.contrib.admin import site, StackedInline  # TabularInline
from django.utils.translation import ugettext_lazy as _
from hvad.admin import TranslatableAdmin
from .models import Category, Place, PlacePicture


class CategoryAdmin(TranslatableAdmin):
    list_display = ('root', 'get_title', 'all_translations', )
    list_display_links = ('get_title', )
    list_filter = ('root', )

    def get_title(self, obj):
        return obj.safe_translation_getter('title', unicode(obj.pk))
    get_title.short_description = _('title')


site.register(Category, CategoryAdmin)


class PlacePictureInlineAdmin(StackedInline):  # TabularInline):
    model = PlacePicture


class PlaceAdmin(TranslatableAdmin):
    inlines = [PlacePictureInlineAdmin, ]
    list_display = ('category', 'get_title', 'premium', 'all_translations', 'qr_code', )
    list_display_links = ('get_title', )
    list_filter = ('category', )

    def get_title(self, obj):
        return obj.safe_translation_getter('title', unicode(obj.pk))
    get_title.short_description = _('title')

    def qr_code(self, obj):
        data = "http://montecatiniterme.ivirgilius.com%s" % obj.get_absolute_url()
        small = "http://api.qrserver.com/v1/create-qr-code/?%s" % urllib.urlencode({'data': data, 'size': "50x50"})
        big = "http://api.qrserver.com/v1/create-qr-code/?%s" % urllib.urlencode({'data': data, 'size': "1000x1000"})
        return "<a href='%s'><img src='%s' width='50' height='50' /></a>" % (big, small)
    qr_code.allow_tags = True


site.register(Place, PlaceAdmin)
