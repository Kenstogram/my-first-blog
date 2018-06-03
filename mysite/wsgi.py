"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
>>>>>>> 37c99181c9a6b95433d60f8c8ef9af5731096435
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
