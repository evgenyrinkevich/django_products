import environ
from .base import *

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']


SITE_ID = ENGLISH_SITE_ID
