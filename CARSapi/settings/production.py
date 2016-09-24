from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'CARSapi_database',
        'USER': 'CARSapi_admin',
        'PASSWORD': '1234567890',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATIC_URL = '/static/'