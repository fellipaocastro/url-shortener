# coding: utf-8
from __future__ import absolute_import, unicode_literals

from .base import *

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-yanc',
    '--with-spec',
    '--spec-color',
    '--with-coverage',
    '--cover-min-percentage=69',
    '--cover-inclusive',
    '--cover-package=shorturls',
]
