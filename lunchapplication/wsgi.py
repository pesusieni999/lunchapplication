"""
WSGI config for lunchapplication project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))

import django.core
import django.core.handlers
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


__author__ = "Ville Myllynen"
__copyright__ = "Copyright 2017, Ohsiha Project"
__credits__ = ["Ville Myllynen"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ville Myllynen"
__email__ = "ville.myllynen@student.tut.fi"
__status__ = "Development"


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lunchapplication.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
