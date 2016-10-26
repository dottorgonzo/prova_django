#coding=utf-8
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields


class RootCategory():
    SHOPPING = 1
    TEMPO_LIBERO = 2
    BERE_E_MANGIARE = 3
    DORMIRE = 4
    SERVIZI = 5
    CHOICES = (
        (SHOPPING, _('Shopping')),
        (TEMPO_LIBERO, _('Free Time')),
        (BERE_E_MANGIARE, _('Food and Drink')),
        (DORMIRE, _('Lodging')),
        (SERVIZI, _('Services')),
    )


class Category(TranslatableModel):
    ts_add = models.DateTimeField(_('date added'), auto_now=False, auto_now_add=True)
    ts_edit = models.DateTimeField(_('last update'), auto_now=True, auto_now_add=True)
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
    )
    root = models.PositiveSmallIntegerField(_('root category'), choices=RootCategory.CHOICES,
                                            help_text=_("The same for all translations."))

    def __unicode__(self):
        name = self.lazy_translation_getter('title', unicode(self.pk))
        return "%s / %s" % (self.get_root_display(), name)

    def get_absolute_url(self):
        return reverse('montecatini_ccn.views.category', None, [self.root, self.id, ])

    class Meta():
        ordering = ('root', )
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Place(TranslatableModel):
    ts_add = models.DateTimeField(_('date added'), auto_now=False, auto_now_add=True)
    ts_edit = models.DateTimeField(_('last update'), auto_now=True, auto_now_add=True)
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
        address=models.CharField(_('address'), max_length=255, blank=True, null=True),
        content=RichTextField(_('content'), config_name='basic_ckeditor', blank=True, null=True),
    )
    category = models.ForeignKey(Category, help_text=_("The same for all translations."))
    premium = models.BooleanField(_('premium'), default=False, help_text=_("The same for all translations."))
    latitude = models.FloatField(_('latitude'), help_text=_("The same for all translations."))
    longitude = models.FloatField(_('longitude'), help_text=_("The same for all translations."))
    email = models.EmailField(_('email'), blank=True, null=True, help_text=_("The same for all translations."))
    url = models.URLField(_('url'), blank=True, null=True, help_text=_("The same for all translations."))
    phone = models.CharField(_('phone'), max_length=25, blank=True, null=True,
                             help_text=_("The same for all translations."))

    def __unicode__(self):
        return self.lazy_translation_getter('title', unicode(self.pk))

    def get_absolute_url(self):
        return reverse('montecatini_ccn.views.place', None, [self.category.root, self.category.id, self.id, ])

    class Meta():
        ordering = ('category__root', 'category', )
        verbose_name = _('place')
        verbose_name_plural = _('places')


class PlacePicture(models.Model):
    ts_add = models.DateTimeField(_('date added'), auto_now=False, auto_now_add=True)
    ts_edit = models.DateTimeField(_('last update'), auto_now=True, auto_now_add=True)
    place = models.ForeignKey(Place)
    picture = models.ImageField(_('picture'), upload_to='places', help_text=_("Si consiglia 640x480 con soggetto centrale. ATTENZIONE: la visualizzazione cambia da dispositivo a dispositivo."))

    class Meta():
        ordering = ('ts_add', )
        verbose_name = _('picture')
        verbose_name_plural = _('pictures')
