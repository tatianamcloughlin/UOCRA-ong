from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3ndsqav6n99th',
        'USER': 'pxkvcfexeyrmsv',
        'PASSWORD': 'a7c65ecc5c8f5039b8e02714cc9dafadf1563b57ff2bd8d2fc2f3630bdb1f3cf',
        'HOST': 'ec2-34-227-135-211.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
import django_heroku
django_heroku.settings(locals())