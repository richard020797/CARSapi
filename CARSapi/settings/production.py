from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'CARSapi_database',
        'USER': 'CARSapi_admin',
        'PASSWORD': '1q2w3e4r',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'/static/')
