from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3s3msuvbbdl0k',
        'USER': 'qjsgcnkakjcsmj',
        'PASSWORD': '69689410e0b1670fc58608300b934086cb8b255af7e1c09abf05caaf8f85429f',
        'HOST': 'ec2-54-159-175-38.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
import django_heroku
django_heroku.settings(locals())