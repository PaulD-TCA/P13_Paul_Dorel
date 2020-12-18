from django.urls import path
from . import views

urlpatterns = [
    path('my_offers/', views.my_offers, name='my_offers'),
    path('messages/', views.messages, name='messages'),
]
