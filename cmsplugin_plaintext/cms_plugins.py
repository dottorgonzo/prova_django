from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import CMSCharFieldPlugin, CMSTextFieldPlugin, CMSEmailFieldPlugin, CMSURLFieldPlugin, \
    CMSPhoneFieldPlugin, CMSGeoPositionFieldPlugin, CMSTextWithTitlePlugin
from djangocms_text_ckeditor.cms_plugins import TextPlugin


class CharFieldPlugin(CMSPluginBase):
    model = CMSCharFieldPlugin
    name = _('One line of text')
    render_template = 'cmsplugin_plaintext/text.html'

    def render(self, context, instance, placeholder):
        context.update({
            'body': instance.body,
            'object': instance,
            'placeholder': placeholder
        })
        return context


class TextFieldPlugin(CMSPluginBase):
    model = CMSTextFieldPlugin
    name = _('Simple text area')
    render_template = 'cmsplugin_plaintext/text.html'

    def render(self, context, instance, placeholder):
        context.update({
            'body': instance.body,
            'object': instance,
            'placeholder': placeholder
        })
        return context


class EmailFieldPlugin(CMSPluginBase):
    model = CMSEmailFieldPlugin
    name = _('Email')
    render_template = 'cmsplugin_plaintext/email.html'

    def render(self, context, instance, placeholder):
        context.update({
            'body': instance.body,
            'object': instance,
            'placeholder': placeholder
        })
        return context


class URLFieldPlugin(CMSPluginBase):
    model = CMSURLFieldPlugin
    name = _('URL')
    render_template = 'cmsplugin_plaintext/url.html'

    def render(self, context, instance, placeholder):
        context.update({
            'body': instance.body,
            'object': instance,
            'placeholder': placeholder
        })
        return context


class PhoneFieldPlugin(CMSPluginBase):
    model = CMSPhoneFieldPlugin
    name = _('Phone number')
    render_template = 'cmsplugin_plaintext/phone.html'

    def render(self, context, instance, placeholder):
        context.update({
            'body': instance.body,
            'object': instance,
            'placeholder': placeholder
        })
        return context


class GeoPositionFieldPlugin(CMSPluginBase):
    model = CMSGeoPositionFieldPlugin
    name = _('GEO Position')
    render_template = 'cmsplugin_plaintext/geo.html'

    def render(self, context, instance, placeholder):
        context.update({
            'latitude': instance.latitude,
            'longitude': instance.longitude,
            'object': instance,
            'placeholder': placeholder
        })
        return context


class TextWithTitlePlugin(TextPlugin):
    model = CMSTextWithTitlePlugin
    render_template = "cmsplugin_plaintext/text_with_title.html"


plugin_pool.register_plugin(CharFieldPlugin)
plugin_pool.register_plugin(TextFieldPlugin)
plugin_pool.register_plugin(EmailFieldPlugin)
plugin_pool.register_plugin(GeoPositionFieldPlugin)
plugin_pool.register_plugin(PhoneFieldPlugin)
plugin_pool.register_plugin(URLFieldPlugin)
plugin_pool.register_plugin(TextWithTitlePlugin)
