"""
Django settings for bfrs_project project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import dj_database_url
import ldap
import os
import sys

from confy import env, database, cache

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CRISPY_TEMPLATE_PACK = 'bootstrap3'
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880 * 4 # 5.0MB * 4

EMAIL_HOST = env('EMAIL_HOST', 'email.host')
EMAIL_PORT = env('EMAIL_PORT', 25)
FROM_EMAIL = env('FROM_EMAIL', 'from_email')
PICA_EMAIL = env('PICA_EMAIL', 'pica_email')
PVS_EMAIL = env('PVS_EMAIL', 'pvs_email')
FPC_EMAIL = env('FPC_EMAIL', 'fpc_email')
POLICE_EMAIL = env('POLICE_EMAIL', 'police_email')
DFES_EMAIL = env('DFES_EMAIL', 'dfes_email')
FSSDRS_EMAIL = env('FSSDRS_EMAIL', 'fssdrs_email')
EMAIL_TO_SMS_FROMADDRESS = env('EMAIL_TO_SMS_FROMADDRESS', 'pics_sms_from')
SMS_POSTFIX = env('SMS_POSTFIX', 'sms_postfix')
MEDIA_ALERT_SMS_TOADDRESS_MAP = env('MEDIA_ALERT_SMS_TOADDRESS_MAP', 'pica_sms_to')
ALLOW_EMAIL_NOTIFICATION = os.environ.get('ALLOW_EMAIL_NOTIFICATION', None) in ["True", "on", "1", "DEBUG"]

INTERNAL_EMAIL = env('INTERNAL_EMAIL', ['dpaw.wa.gov.au'])
SSS_URL = env('SSS_URL', 'sss_redirect_url')
AREA_THRESHOLD = env('AREA_THRESHOLD', 2)

URL_SSO = env('URL_SSO', 'https://oim.dpaw.wa.gov.au/api/users/')
USER_SSO = env('USER_SSO')
PASS_SSO = env('PASS_SSO')
FSSDRS_USERS = env('FSSDRS_USERS')
FSSDRS_GROUP = env('FSSDRS_GROUP', 'FSS Datasets and Reporting Services')

HARVEST_EMAIL_HOST = env('HARVEST_EMAIL_HOST')
HARVEST_EMAIL_USER = env('HARVEST_EMAIL_USER')
HARVEST_EMAIL_PASSWORD = env('HARVEST_EMAIL_PASSWORD')

# Outstanding Fires Report
GOLDFIELDS_EMAIL = env('GOLDFIELDS_EMAIL', 'goldfields_email')
KIMBERLEY_EMAIL = env('KIMBERLEY_EMAIL', 'kimberley_email')
MIDWEST_EMAIL = env('MIDWEST_EMAIL', 'midwest_email')
PILBARA_EMAIL = env('PILBARA_EMAIL', 'pilbara_email')
SOUTH_COAST_EMAIL = env('SOUTH_COAST_EMAIL', 'south_coast_email')
SOUTH_WEST_EMAIL = env('SOUTH_WEST_EMAIL', 'south_west_email')
SWAN_EMAIL = env('SWAN_EMAIL', 'swan_email')
WARREN_EMAIL = env('WARREN_EMAIL', 'warren_email')
WHEATBELT_EMAIL = env('WHEATBELT_EMAIL', 'wheatbelt_email')
OUTSTANDING_FIRES_EMAIL=[ 
    {"Goldfields": GOLDFIELDS_EMAIL}, 
    {"Kimberley": KIMBERLEY_EMAIL},
    {"Midwest": MIDWEST_EMAIL},
    {"Pilbara": PILBARA_EMAIL},
    {"South Coast": SOUTH_COAST_EMAIL},
    {"South West": SOUTH_WEST_EMAIL},
    {"Swan": SWAN_EMAIL},
    {"Warren": WARREN_EMAIL},
    {"Wheatbelt": WHEATBELT_EMAIL},
]
#if ALL_REGIONS_EMAIL: OUTSTANDING_FIRES_EMAIL.append({"All Regions": ALL_REGIONS_EMAIL})
     

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
#SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = os.environ.get('DEBUG', None) in ["True", "on", "1", "DEBUG"]

ALLOWED_HOSTS = []

#DEBUG = os.environ.get('DEBUG', None) in ["True", "on", "1", "DEBUG"]
INTERNAL_IPS = ['127.0.0.1', '::1']
if not DEBUG:
    # Localhost, UAT and Production hosts
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
        'bfrs.dpaw.wa.gov.au',
        'bfrs.dpaw.wa.gov.au.',
        'bfrs-uat.dpaw.wa.gov.au',
        'bfrs-uat.dpaw.wa.gov.au.',
        'bfrs-uat.dbca.wa.gov.au',
        'bfrs-uat.dbca.wa.gov.au.',
        'bfrs-dev.dpaw.wa.gov.au',
        'bfrs-dev.dpaw.wa.gov.au.',
        'bfrs-dev.dbca.wa.gov.au',
        'bfrs-dev.dbca.wa.gov.au.',
        'aws-oim-001',
        'aws-oim-001.',
        '192.168.0.4',
        '192.168.0.4.',
    ]

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'bfrs.dpaw.wa.gov.au',
    'bfrs.dpaw.wa.gov.au.',
    'bfrs-uat.dpaw.wa.gov.au',
    'bfrs-uat.dpaw.wa.gov.au.',
    'bfrs-uat.dbca.wa.gov.au',
    'bfrs-uat.dbca.wa.gov.au.',
    'bfrs-dev.dpaw.wa.gov.au',
    'bfrs-dev.dpaw.wa.gov.au.',
    'bfrs-dev.dbca.wa.gov.au',
    'bfrs-dev.dbca.wa.gov.au.',
    'aws-oim-001',
    'aws-oim-001.',
    '192.168.0.4',
    '192.168.0.4.',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    #'guardian',
    'reversion',
    'reversion_compare',
    'tastypie',
    'smart_selects',
    'django_extensions',
    'debug_toolbar',
    'crispy_forms',
    'django_filters',

    'bfrs',
]

ADD_REVERSION_ADMIN=True

MIDDLEWARE_CLASSES = [
#    'django.middleware.security.SecurityMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
#    'dpaw_utils.middleware.SSOLoginMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'dpaw_utils.middleware.SSOLoginMiddleware',

]

ROOT_URLCONF = 'bfrs_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'bfrs', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
#            'loaders': [
#                'django.template.loaders.cached.Loader',
#                'django.template.loaders.filesystem.Loader',
#                'django.template.loaders.app_directories.Loader',
#            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'bfrs_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {'default': database.config()}
#DATABASES = {'default': dj_database_url.config()}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'guardian.backends.ObjectPermissionBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Australia/Perth'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
         'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'compressor.finders.CompressorFinder',

)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            #'stream': sys.stdout,
            'formatter': 'verbose',
        },
        'file': {
            'level': 'INFO',
            #'class': 'logging.FileHandler',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/bfrs.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'bfrs': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    }

}

if DEBUG:
    LOGGING['loggers']['django.request']['level'] = 'DEBUG'
    LOGGING['loggers']['bfrs']['level'] = 'DEBUG'


