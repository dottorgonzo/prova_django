# -*- coding: utf-8 -*-
import os
import socket
import sys

gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('Francesco Facconi', 'francesco@immediatic.it'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'montecatiniterme',
        'USER': 'ivirgilius',
        'PASSWORD': '8Mkjmdh6BL',
        'HOST': '127.0.0.1',
        'PORT': '',
        'TEST_CHARSET': 'UTF8'
    },
}

TIME_ZONE = 'Europe/Rome'
#LANGUAGE_CODE = 'it-it'
LANGUAGE_CODE = 'it'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

ALLOWED_HOSTS = ['.montecatiniterme.ivirgilius.com', ]

MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_PATH, "resources")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'g=piypg8kn&amp;=_7^#ht-9hxw%0qc*6-m8hlg%bj0ez7e*lv^-mf'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ## IF CACHE MIDDLEWARE IS SETTING PUT HERE
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'montecatini.middleware.MobileDetectionMiddleware',
)

ROOT_URLCONF = 'montecatini.urls'

WSGI_APPLICATION = 'montecatini.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'django.contrib.markup',
    'django.contrib.admindocs',

    'djangocms_text_ckeditor',
    'ckeditor',

    'ordered_model',
    'hvad',  # http://django-hvad.readthedocs.org/en/latest/index.html
    'rosetta',

    'cms',
    #'cms.stacks',
    'mptt',
    'menus',
    'south',
    'sekizai',

    'djangocms_file',
    #'djangocms_flash',
    #'djangocms_googlemap',
    'djangocms_link',
    'djangocms_picture',
    #'cms.plugins.snippet',
    #'cms.plugins.teaser',
    #'cms.plugins.text',
    'djangocms_video',
    #'cms.plugins.twitter',

    #'filer',
    #'cmsplugin_filer_file',
    #'cmsplugin_filer_folder',
    #'cmsplugin_filer_image',
    #'cmsplugin_filer_teaser',
    #'cmsplugin_filer_video',

    'cmsplugin_plaintext',
    'cmsplugin_youtube',

    'montecatini_ccn',
    'montecatini_events',
    'montecatini_map',
    'montecatini_metro',
    'montecatini_news',

    'templateaddons',
    'south',
    'easy_thumbnails',
    
    'gunicorn',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

USE_ETAGS = True
SEND_BROKEN_LINK_EMAILS = False
PREPEND_WWW = False
APPEND_SLASH = True
FIRST_DAY_OF_WEEK = 1

LOGIN_REDIRECT_URL = "/"
#LOGIN_URL = "/login/"
#LOGOUT_URL = "/logout/"

MODEL_I18N_MASTER_LANGUAGE = 'it'
#https://github.com/jaddison/django-multihost
#MULTIHOST_REDIRECT_URL = "http://www.immediatic.it/"
#MULTIHOST_AUTO_WWW = True

GRAPPELLI_ADMIN_TITLE = "iVirgilius"

TINYMCE_FILEBROWSER = True
TINYMCE_COMPRESSOR = False
TINYMCE_SPELLCHECKER = False

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "spellchecker,paste,searchreplace",
    'theme': "advanced",
    'theme_advanced_buttons1': "bold,italic,underline,separator,pastetext,pasteword",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_path': False,
    'theme_advanced_statusbar_location': "none",
    'theme_advanced_blockformats': "p,h1,h2",
    'font_size_style_values': "10px,12px,14px,16px,18px,20px",
    'theme_advanced_font_sizes': "10px,12px,14px,16px,18px,20px",
    'width': '320',
    'height': '240',
    'cleanup_on_startup': True,
    'paste_auto_cleanup_on_paste': True,
    'custom_undo_redo_levels': 10,
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

THUMBNAIL_BASEDIR = 'eth'

CMS_TEMPLATES = (
    ('templates/default.html', 'Predefinita'),
    ('templates/home.html', 'Home page'),
    ('templates/ccn_default.html', 'CCN - Informazioni'),
)

LANGUAGES = (
    ('it', gettext('Italian')),
    ('en', gettext('English')),
    ('de', gettext('German')),
    ('es', gettext('Spanish')),
    ('ru', gettext('Russian')),
    ('fr', gettext('French')),
    ('zh', gettext('Chinese')),
)

#https://github.com/divio/djangocms-text-ckeditor
CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar': 'CMS',
    'skin': 'moono',
    'forcePasteAsPlainText': True,
    'pasteFromWordRemoveFontStyles': True,
}

#TEXT_SAVE_IMAGE_FUNCTION = 'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

CMS_PLACEHOLDER_CONF = {
    'event_icon': {
        'plugins': [
            'PicturePlugin',
        ],
        'extra_context': {"width": 190},
        'name': 'Icona',
        'limits': {"global": 1}
    },
    'event_description': {
        'plugins': [
            'CharFieldPlugin',
        ],
        'name': 'Informazioni principali',
        'limits': {"global": 2}
    },
    'content': {
        'plugins': [
            'TextPlugin',
            'PicturePlugin',
            'FilePlugin',
        ],
        'name': "Contenuto"
    },
    'news_content': {
        'plugins': [
            'TextPlugin',
            #'PicturePlugin',
        ],
        'name': "Contenuto"
    },
    'event_content': {
        'plugins': [
            'TextPlugin',
            #'PicturePlugin',
        ],
        'name': "Contenuto"
    },
    'ccn_content': {
        'plugins': [
            'TextPlugin',
            #'PicturePlugin',
        ],
        'name': "Contenuto"
    },

    'details_address': {
        'plugins': ['CharFieldPlugin', ],
        'name': 'Indirizzo',
        'limits': {"global": 1}
    },
    'details_phone': {
        'plugins': ['PhoneFieldPlugin', ],
        'name': 'Telefono',
        'limits': {"global": 1}
    },
    'details_email': {
        'plugins': ['EmailFieldPlugin', ],
        'name': 'Email',
        'limits': {"global": 1}
    },
    'details_url': {
        'plugins': ['URLFieldPlugin', ],
        'name': 'Sito internet',
        'limits': {"global": 2}
    },
    'details_geolocation': {
        'plugins': ['GeoPositionFieldPlugin', ],
        'name': 'Coordinate geografiche',
        'limits': {"global": 2}
    },

    'poi_audio': {
        'plugins': ['FilePlugin', ],
        'name': 'Audio Guida (caricare file .mp3)',
        'limits': {"global": 1}
    },
    'poi_video': {
        'plugins': ['YouTubePlugin', ],
        'name': 'Video di presentazione (YouTube)',
        'limits': {"global": 1}
    },
    'subcontent': {
        'plugins': ['TextWithTitlePlugin', ],
        'name': 'Contenuti Extra',
    },

}

ROSETTA_STORAGE_CLASS = 'rosetta.storage.SessionRosettaStorage'

CKEDITOR_UPLOAD_PATH = os.path.join(PROJECT_PATH, "media")
CKEDITOR_CONFIGS = {
    'basic_ckeditor': {
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic', '-', 'Link', 'Unlink']
        ],
        'toolbar': 'Basic',
        'width': '320',
        'height': '320',
        'forcePasteAsPlainText': True,
        'pasteFromWordRemoveFontStyles': True,
    },
}

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, "montecatini", "locale"),
    os.path.join(PROJECT_PATH, "montecatini_ccn", "locale"),
    os.path.join(PROJECT_PATH, "montecatini_events", "locale"),
    os.path.join(PROJECT_PATH, "montecatini_map", "locale"),
    os.path.join(PROJECT_PATH, "montecatini_metro", "locale"),
    os.path.join(PROJECT_PATH, "montecatini_news", "locale"),
)


try:
    from local_settings import *
except ImportError:
    pass
