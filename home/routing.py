from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/pizza/<order_id>',consumers.OrderProgress.as_asgi()),
]