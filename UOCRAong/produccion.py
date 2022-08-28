from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd4e0qa2am1kblv',
        'USER': 'jmcbaoqaqfuycm',
        'PASSWORD': 'a6976cf595c27aa3879a094d40cafcef073f8401787b796906e3ec2cebe643cb',
        'HOST': 'ec2-44-194-117-205.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
import django_heroku
django_heroku.settings(locals())