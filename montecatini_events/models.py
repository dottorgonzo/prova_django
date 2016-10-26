#coding=utf-8
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields


class Event(TranslatableModel):
    def _get_size(self):
        return self.lazy_translation_getter('title', unicode(self.pk))

    ts_add = models.DateTimeField(_('date added'), auto_now=False, auto_now_add=True)
    ts_edit = models.DateTimeField(_('last update'), auto_now=True, auto_now_add=True)
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
        subtitle1=models.CharField(_('subtitle 1'), max_length=255),
        subtitle2=models.CharField(_('subtitle 2'), max_length=255, blank=True, null=True),
        content=RichTextField(_('content'), config_name='basic_ckeditor', blank=True, null=True),
    )
    published = models.BooleanField(_('published'), default=True, help_text=_("The same for all translations."))
    picture = models.ImageField(_('picture'), blank=True, null=True, upload_to='events',
                                help_text=_("The same for all translations. Si consiglia 250x250 pixel, PNG o JPG."))
    details_picture = models.ImageField(_('details picture'), blank=True, null=True, upload_to='events',
                                        help_text=_("The same for all translations. xSi consiglia 640x480 pixel con soggetto centrale, PNG o JPG. ATTENZIONE: la visualizzazione cambia da dispositivo a dispositivo."))

    def __unicode__(self):
        return self.lazy_translation_getter('title', unicode(self.pk))

    def get_absolute_url(self):
        return reverse('montecatini_events.views.event', None, [self.id, ])

    class Meta():
        ordering = ('-ts_add',)
        verbose_name = _('event')
        verbose_name_plural = _('events')
