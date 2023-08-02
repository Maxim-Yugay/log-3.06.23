"""
Django settings for news project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rd=6jx@g65$pt7hrb#ba7bf$z@9xsx3ovn4o8z#zw4-ruymr49'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
    'rest_framework',

    'board',
    'accounts',
    'news_paper',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'basic.middlewares.TimezoneMiddleware',

]

ROOT_URLCONF = 'news.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGES = [
    ('ru', 'Русский'),
    ('en-us', 'English')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'news.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

LOGIN_REDIRECT_URL = "/news"
LOGOUT_REDIRECT_URL = '/news'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    ]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

ACCOUNT_FORMS = {'signup': 'accounts.forms.CustomSignupForm'}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "yugay.maxim"
EMAIL_HOST_PASSWORD = "jlrubecsauiswkhu"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "yugay.maxim@yandex.ru"

SERVER_EMAIL = 'example@yandex.ru'

MANAGERS = (
    ('Billy', 'Billy@Billy.com')
)
ADMINS = (
    ('Jimmy', 'Jimmy@Jimmy.com')
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CELERY_BROKER_URL = 'redis://default:'\
    'o28atVVjLKmlPdvEmCQApmXWNCJNTuqZ@redis-12290.c302.asia-northeast1-1.gce.cloud.redislabs.com:12290'
CELERY_RESULT_BACKEND = 'redis://default:'\
    'o28atVVjLKmlPdvEmCQApmXWNCJNTuqZ@redis-12290.c302.asia-northeast1-1.gce.cloud.redislabs.com:12290'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        'TIMEOUT': 60,

    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'console_d': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
        'console_w': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },
        'console_ec': {
            'format': '{asctime} {levelnaem} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'genlog': {
            'format': '{asctime} {levelnaem} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'filters': ['debug_true'],
            'level': 'DEBUG',
            'formatter': 'console_d',
            'class': 'logging.StreamHandler',
        },
        'consoleW': {
            'filters': ['debug_true'],
            'level': 'WARNING',
            'formatter': 'console_w',
            'class': 'logging.StreamHandler',
        },
        'consoleEC': {
            'filters': ['debug_true'],
            'level': ['ERROR', 'CRITICAL'],
            'formatter': 'console_ec',
            'class': 'logging.StreamHandler',
        },
        'gen': {
            'filters': ['debug_false'],
            'level': 'INFO',
            'formatter': 'genlog',
            'filename': 'general.log',
            'class': 'logging.FileHandler',
        },
        'err': {
            'filters': ['debug_true'],
            'level': ['ERROR', 'CRITICAL'],
            'formatter': 'console_w',
            'filename': 'errors.log',
            'class': 'logging.FileHandler',
        },
        'sec': {
            'filters': ['debug_true'],
            'level': ['WARNING', 'ERROR'],
            'formatter': 'genlog',
            'filename': 'security.log',
            'class': 'logging.FileHandler',
        },
        'mail': {
            'filters': ['debug_false'],
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'console_w',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'consoleW', 'consoleEC', 'gen'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['err', 'mail'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['err'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['err'],
            'leve': 'err',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['sec'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail', 'err'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}
