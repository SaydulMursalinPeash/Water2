"""
ASGI config for Water project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import django
from channels.routing import get_default_application
from django.core.wsgi import get_wsgi_application
from Water.settings import CHANNEL_LAYERS
from sensor.routings import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Water.settings')
wsgi_app=get_wsgi_application()
asgi_app=get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})

# Use pre-defined channel layer
channel_layer = CHANNEL_LAYERS['redis']