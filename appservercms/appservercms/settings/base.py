"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

ALLOWED_HOSTS = ['localhost', 'green']

# Application definition

INSTALLED_APPS = [

    'adminextend',
    'search',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'wagtail.contrib.table_block',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'blog',
    'html5up',
    'home',

    # last application to finalize things
    'finalware'

]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'appservercms.urls'

OPTIONS={
    'libraries': {
        'home_tags': 'home.tags',
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
            os.path.join(PROJECT_DIR, 'blog', 'templates'),
            os.path.join(PROJECT_DIR, 'html5up', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'finalware.context_processors.contextify'
            ],
        },
    },
]

WSGI_APPLICATION = 'appservercms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'appserver',
        'USER':  'appserver',
        'PASSWORD': os.environ['POSTGRES_CMSDB_PASSWORD'],
        'HOST': os.environ['POSTGRES_CMSDB_HOST'],
        'PORT': 5432},
}
#DATABASE_ROUTERS = ['apps.dbrouter.AuthRouter',]



# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

#STATICFILES_DIRS = [
#    os.path.join(PROJECT_DIR, 'static'),
#]

STATIC_ROOT = os.path.join("/home/service", "static/")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join("/home/appserver/media/cmsdb/")
MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "inchiresolvercms"

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch5',
        'URLS': ['http://cmsindex:9200'],
        'INDEX': 'wagtail',
        'TIMEOUT': 5,
        'AUTO_UPDATE': True,
    }
}

WAGTAILIMAGES_MAX_UPLOAD_SIZE = 75 * 1024 * 1024  # i.e. 20MB

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = os.environ['DJANGO_HOSTNAME']


META_SITE_PROTOCOL = 'http'
META_USE_SITES = True


SITE_OBJECTS_INFO_DICT = {
    '1': {
        'name': os.environ['DJANGO_HOSTNAME'],
        'domain': os.environ['DJANGO_HOSTNAME'],
    },
}
SITE_ID = 1


# To create/update a superuser account automatically, add the following to your settings file.
# This will disable the `superuser` creation option of syncdb.

# This field is the superuser object ID. Pick something other than `1` for security reason.
SITE_SUPERUSER_ID = '987'

# This field is stored in `User.USERNAME_FIELD`. This is usually a `username` or  an `email`.
SITE_SUPERUSER_USERNAME = 'djangoadmin'

# This field is stored in the `email` field, provided, that `User.USERNAME_FIELD` is not an `email`.
# If `User.USERNAME_FIELD` is already an email address, set `SITE_SUPERUSER_EMAIL = SITE_SUPERUSER_USERNAME`
SITE_SUPERUSER_EMAIL = 'django@django'

# A hashed version of `SITE_SUPERUSER_PASSWORD` will be store in superuser's `password` field.
SITE_SUPERUSER_PASSWORD = 'djangoDJANGO'








