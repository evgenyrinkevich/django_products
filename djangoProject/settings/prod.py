import environ
from .base import *

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

SITE_ID = ENGLISH_SITE_ID

STATIC_URL = "/static/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'products',
        'USER': 'django',
        'PASSWORD': 'geekbrains',
        'HOST': 'db',
        'PORT': '5432',
    }
}
