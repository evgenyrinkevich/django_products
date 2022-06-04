from .dev import *

# test dev server with postgres_db in docker container

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'products',
        'USER': 'django',
        'PASSWORD': 'geekbrains',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
