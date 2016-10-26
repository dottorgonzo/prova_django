#coding=utf-8
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields
from ordered_model.models import OrderedModel


class Areas():
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'
    CHOICES = (
        (RED, _('Red Line')),
        (YELLOW, _('Yellow Line')),
        (GREEN, _('Green Line')),
        (BLUE, _('Blue Line')),
    )


class Lines():
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'
    CHOICES = (
        (RED, _('Red Line')),
        (YELLOW, _('Yellow Line')),
        (GREEN, _('Green Line')),
        (BLUE, _('Blue Line')),
    )


class PointOfInterest(TranslatableModel, OrderedModel):
    ts_add = models.DateTimeField(_('date added'), auto_now=False, auto_now_add=True)
    ts_edit = models.DateTimeField(_('last update'), auto_now=True, auto_now_add=True)
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
        content=RichTextField(_('content'), config_name='basic_ckeditor'),
        youtube_id=models.CharField(_('YouTube ID'), max_length=15, blank=True, null=True),
        mp3=models.FileField(_('mp3 audio'), upload_to='mp3', blank=True, null=True)
    )
    line = models.CharField(_('line'), max_length=25, choices=Lines.CHOICES,
                            help_text=_("The same for all translations."))

    latitude = models.FloatField(_('latitude'), help_text=_("The same for all translations."))
    longitude = models.FloatField(_('longitude'), help_text=_("The same for all translations."))

    def __unicode__(self):
        return self.lazy_translation_getter('title', unicode(self.pk))

    def get_absolute_url(self):
        url = "%s#%s" % (reverse('montecatini_metro.views.line', None, [self.line, ]), self.id)
        return url

    class Meta(OrderedModel.Meta):
        verbose_name = _('point of interest')
        verbose_name_plural = _('points of interests')


class SubContent(TranslatableModel):
    ts_add = models.DateTimeField(_('date added'), auto_now=False, auto_now_add=True)
    ts_edit = models.DateTimeField(_('last update'), auto_now=True, auto_now_add=True)
    poi = models.ForeignKey(PointOfInterest)
    ordering = models.PositiveSmallIntegerField(_('ordering'), default=0, help_text=_("The same for all translations."))
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
        content=RichTextField(_('content'), config_name='basic_ckeditor'),
    )

    def __unicode__(self):
        return self.lazy_translation_getter('title', unicode(self.pk))

    def get_absolute_url(self):
        url = "%s#%s" % (reverse('montecatini_metro.views.line', None, [self.line, ]), self.id)
        return url

    class Meta:
        verbose_name = _('subcontent')
        verbose_name_plural = _('subcontents')


class Picture(models.Model):
    ts_add = models.DateTimeField(_('date added'), auto_now=False, auto_now_add=True)
    ts_edit = models.DateTimeField(_('last update'), auto_now=True, auto_now_add=True)
    poi = models.ForeignKey(PointOfInterest)
    image = models.ImageField(_('image'), upload_to='poi', help_text=_("The same for all translations. Si consiglia 640x480 pixel con soggetto centrale, PNG o JPG. ATTENZIONE: la visualizzazione cambia da dispositivo a dispositivo."))
    ordering = models.PositiveSmallIntegerField(_('ordering'), default=0, help_text=_("The same for all translations."))

    class Meta:
        ordering = ('poi', 'ordering')
        verbose_name = _('picture')
        verbose_name_plural = _('pictures')


class SliderPicture(OrderedModel):
    ts_add = models.DateTimeField(_('date added'), auto_now=False, auto_now_add=True)
    ts_edit = models.DateTimeField(_('last update'), auto_now=True, auto_now_add=True)
    area = models.CharField(_('area'), max_length=25, choices=Areas.CHOICES,
                            help_text=_("The same for all translations."))
    image = models.ImageField(_('image'), upload_to='slider', help_text=_("The same for all translations. Si consiglia 640x480 pixel con soggetto centrale, PNG o JPG. ATTENZIONE: la visualizzazione cambia da dispositivo a dispositivo."))

    class Meta(OrderedModel.Meta):
        verbose_name = _('picture for slider')
        verbose_name_plural = _('pictures for slider')
