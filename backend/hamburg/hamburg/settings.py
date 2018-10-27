"""
Django settings for hamburg project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from ast import literal_eval as le
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
IS_PROD = le(os.environ.get('IS_PROD', 'True'))
DEBUG = not IS_PROD

MOVIEDB_API_KEY = os.environ['MOVIEDB_API_KEY']
MOVIEDB_API_BASE = os.environ['MOVIEDB_API_BASE']
MOVIEDB_API_SEARCH = os.environ['MOVIEDB_API_SEARCH']
MOVIEDB_API_REGION = os.environ['MOVIEDB_API_REGION']
MOVIEDB_API_LANG = os.environ['MOVIEDB_API_LANG']
MOVIEDB_API_DETAILS = os.environ['MOVIEDB_API_DETAILS']
MOVIEDB_API_SHOWTIMES = os.environ['MOVIEDB_API_SHOWTIMES']
MOVIEDB_API_VIDEO = os.environ['MOVIEDB_API_VIDEO']
MOVIEDB_API_UPCOMING = os.environ['MOVIEDB_API_UPCOMING']
MOVIEDB_API_POPULAR = os.environ['MOVIEDB_API_POPULAR']
MOVIEDB_API_NOW_PLAYING = os.environ['MOVIEDB_API_NOW_PLAYING']
MOVIEDB_API_SIMILAR = os.environ['MOVIEDB_API_SIMILAR']
MOVIEDB_API_RECO = os.environ['MOVIEDB_API_RECO']
ALERT_THRESHOLD = le(os.environ['ALERT_THRESHOLD'])

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hamburg_api',
    'rest_framework',
    'gunicorn',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hamburg.urls'
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'hamburg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True),
}
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'vb': {
            'format':"%(levelname)s %(asctime)s %(name)s.%(funcName)s:%(lineno)s- %(message)s"
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.environ.get('LOG_FILE_LOCATION', '/tmp/hamburg_api.log'),
            'formatter': 'vb'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django': {
            'handlers': ['file', 'console'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'user': '50/day',
        'anon': '50/day',
    }
}
