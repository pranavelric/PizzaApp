from .views import *
from django.urls import path

urlpatterns = [
     path('',Home.as_view(),name='home'),
     path('api/order/',OrderPizza.as_view(),name='order_pizza'),
     path('<id>/',OrderPizzaView.as_view(),name='order')
]
