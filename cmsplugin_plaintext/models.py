from django.utils.translation import ugettext as _
from django.db import models
from cms.models import CMSPlugin
from djangocms_text_ckeditor.models import Text


class CMSCharFieldPlugin(CMSPlugin):
    body = models.CharField(_('text'), max_length=500)

    def __unicode__(self):
        return u'%s' % (self.body,)


class CMSTextFieldPlugin(CMSPlugin):
    body = models.TextField(_('text'), help_text='Please use &lt;br/&gt; to break line.')

    def __unicode__(self):
        return u'%s' % (self.body,)


class CMSEmailFieldPlugin(CMSPlugin):
    body = models.EmailField(_('email'))

    def __unicode__(self):
        return u'%s' % (self.body,)


class CMSURLFieldPlugin(CMSPlugin):
    body = models.URLField(_('url'))

    def __unicode__(self):
        return u'%s' % (self.body,)


class CMSPhoneFieldPlugin(CMSPlugin):
    body = models.CharField(_('phone'), max_length=25)

    def __unicode__(self):
        return u'%s' % (self.body,)


class CMSGeoPositionFieldPlugin(CMSPlugin):
    latitude = models.FloatField(_('latitude'))
    longitude = models.FloatField(_('longitude'))

    def __unicode__(self):
        return u'%s, %s' % (self.latitude, self.longitude)


class CMSTextWithTitlePlugin(Text):
    title = models.CharField(_('title'), max_length=255)
