# coding: utf-8
from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.getenv('STATIC_ROOT', BASE_DIR.child('staticfiles'))

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
