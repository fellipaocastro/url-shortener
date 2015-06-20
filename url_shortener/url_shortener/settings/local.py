# coding: utf-8
from __future__ import absolute_import, unicode_literals

from .base import *

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
