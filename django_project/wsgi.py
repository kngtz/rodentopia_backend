"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import dj_database_url

from django.core.wsgi import get_wsgi_application


DATABASES = {'default': dj_database_url.config(
    default='postgres://tjafycozcsiqzs:8f9a576e793fbe4f3bcc06dd0b887ea0454318c3f7d73085dcd3f48d606aee2a@ec2-54-80-184-43.compute-1.amazonaws.com:5432/d3k89ctqpr9dic')}
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = get_wsgi_application()
