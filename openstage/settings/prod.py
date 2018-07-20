from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'openstage',
        'USER': 'postgres',
        'PASSWORD': 'vfi46kb@zc',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}