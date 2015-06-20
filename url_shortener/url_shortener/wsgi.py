# coding: utf-8
from __future__ import absolute_import, unicode_literals
import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'url_shortener.settings.production')

application = get_wsgi_application()

if settings.STATIC_ROOT and settings.STATICFILES_STORAGE:
    from whitenoise.django import DjangoWhiteNoise

    application = DjangoWhiteNoise(application)
