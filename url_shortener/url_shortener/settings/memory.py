# coding: utf-8
from __future__ import absolute_import, unicode_literals

from .test import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
