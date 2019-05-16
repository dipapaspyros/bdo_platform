"""
Django settings for bdo_platform project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import uuid

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i-lcdaw&=80_zgbc&^1(0p&)a2(joi^@*!4(8-%zk^u4s+g@4r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['bdo-dev.epu.ntua.gr', 'localhost']


# Application definition

INSTALLED_APPS = [
    # django
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    # authentication
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # maps
    'leaflet',

    # s3
    's3direct',

    # vizualisations
    'django_nvd3',
    'djangobower',
    'ckeditor',
    'ckeditor_uploader',

    #scheduled_tasks
    'background_task',

    # apps
    'bdo_main_app',
    'bdo_profile',
    'aggregator',
    'query_designer',
    'hcmr_pilot',
    'analytics',
    'visualizer',
    'dashboard_builder',
    'service_builder',
    'note_builder',
    'uploader',
    'on_demand',
    'data_parser',
    'feedback_form',
    'access_controller',
    'wave_energy_pilot',

#     GOOGLE ANALYTICS
    'google_analytics',
    'website_analytics'
]

GOOGLE_ANALYTICS = {
    'google_analytics_id': 'UA-139868802-3',
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1
LOGIN_REDIRECT_URL = '/bdo/'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

    'bdo_main_app.middleware.LoginRequiredMiddleware',
]

LOGIN_EXEMPT_URLS = (
    r'^$',
    r'^about$',
    r'^register$',
    r'^accounts/',
    r'^service_builder/api/createInputFileForHCMRSpillSimulator/',
    r'^service_builder/api/checkIfOutputExistsforHCMRSpillSimulator/',
    r'^wave-energy/energy_conversion/get_load_matching_file_data/'
)

CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
      'LOCATION': '127.0.0.1:11211',
   }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ''


ROOT_URLCONF = 'bdo_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'templates', 'allauth')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bdo_platform.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Django-bower
# ------------

# Specifie path to components root (you need to use absolute path)
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

BOWER_PATH = '/usr/local/bin/bower'

BOWER_INSTALLED_APPS = (
    'd3#3.3.13',
    'nvd3#1.7.1',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
#STATICFILES_FINDERS = (
#'django.contrib.staticfiles.finders.FileSystemFinder',
#'django.contrib.staticfiles.finders.AppDirectoriesFinder',    #causes verbose duplicate notifications in django 1.9
#)


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = 'staticfiles'

# Use manifest static storage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m%d'
USE_L10N = False

#ck editor settings
#CKEDITOR_BASEPATH = "/staticfiles/ckeditor"
CKEDITOR_UPLOAD_PATH ='uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

# bdo main app settings
DATASET_DIR = os.path.join(os.path.join(BASE_DIR, 'aggregator'), 'datasets')
if not os.path.isdir(DATASET_DIR):
    os.mkdir(DATASET_DIR)


# s3
AWS_STORAGE_BUCKET_NAME = 'bdo-platform'

# The region of your bucket, more info:
# http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region
S3DIRECT_REGION = 'eu-central-1'

S3DIRECT_DESTINATIONS = {
    # Allow users to upload their own avatars
    'avatars': {
        'key': lambda filename: 'avatars/' + str(uuid.uuid4().hex) + '.' + filename.split('.')[-1],
        'auth': lambda u: u.is_authenticated(),
    },
}

# add keys
try:
    from .keys import *
except:
    from .keys_example import *
