import os
from django.template import Engine
from .settings import *

DEBUG = True

SECRET_KEY = 'django-insecure-f5-pf*wb$xqo35#krp%4qs(a^h5a^-c8gw=b_g+5qf3)p*cul2'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join (BASE_DIR, 'db.sqlite3')
    }
}