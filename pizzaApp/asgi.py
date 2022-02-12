

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from django.core.asgi import get_asgi_application
import home.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzaApp.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': URLRouter(
           home.routing.websocket_urlpatterns
        )
    }
)