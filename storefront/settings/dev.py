from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-w7zai)ps2^_61*vaib7wjo&1m$sd5mz$s-kqs&ralvu-9z#)cb'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront2',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '0x137716'
    }
}
