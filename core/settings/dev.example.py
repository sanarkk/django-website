from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "*",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dev_db',
        'USER': 'dev_user',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
    }
}