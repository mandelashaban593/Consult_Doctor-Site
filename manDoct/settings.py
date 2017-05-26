# Django settings for tango_with_django_project project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os

import django.conf.global_settings as DEFAULT_SETTINGS
LOCALHOST = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG


LIVE = 1

ADMINS = (
    ('Mandela Shaban', 'mandelashaban@gmail.com'),
)

APP_EMAILS = {

    'info':'mandelashaban@gmail.com',

    }

DEBUG_EMAILS = {

    'mandelashaban@gmail.com' ,

}

BASE_URL = 'https://es-doctor.com/'


APP_NAME = 'es-doctor'
DOMAIN_NAME = 'es-doctor'
APP_TITLE = 'Es-doctor | Consult a doctor online'

MANAGERS = ADMINS


SETTINGS_DIR = os.path.dirname(__file__)

PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)

TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

TEMPLATE_DOCT_PATH = os.path.join(PROJECT_PATH, 'doct_admin/templates/')
TEMPLATE_DOCT_ADMIN_PATH = os.path.join(PROJECT_PATH, 'doct_admin/templates/admin/')

STATIC_PATH = os.path.join(PROJECT_PATH,'static')

DATABASE_PATH = os.path.join(PROJECT_PATH, 'Doct.db')

LOGIN_URL = '/Doct/login/'

SESSION_COOKIE_AGE=1814400

from django.conf import settings

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)) + '/'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'doct_db',
        'USER': 'doctuser',
        'PASSWORD': 'doctpassword',
        'HOST': '',
        'PORT': '',
    }
}


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']


TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True



# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media') # Absolute path to the media d$

MEDIA_URL = BASE_URL + 'static/uploads/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'jah)pvlys_%r_($1!9j&f8ris0g!ow*_k4sesbaqy33!^i@+rx'


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
   
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'manDoct.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'manDoct.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/te$
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
    TEMPLATE_DOCT_PATH,
    TEMPLATE_DOCT_ADMIN_PATH
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'Doct',
    'doct_admin',
    'djangoChat',
    'firebase_cloud_msging',

)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'



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



TWI_ACCOUNT_SID = ""
TWI_AUTH_TOKEN=""

APP_EMAILS = {
    'info':'mandelashaban593@gmail.com',


    }


DISABLE_COMMS = False


PAGNATION_LIMIT = 10
PAGNATION_LIMIT2 = 100



STATIC_ROOT = BASE_DIR + 'static'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = BASE_URL + 'static/'

LOCALHOST = False

AJAX_TEMPLATE_DIR = BASE_DIR + 'templates/Doct/'



BROKER_URL = 'amqp://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'






SITE_ID = 1


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')





try:
    from local_settings import *
except ImportError:
    pass


    