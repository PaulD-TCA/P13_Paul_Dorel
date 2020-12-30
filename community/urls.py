from django.urls import path
from . import views

urlpatterns = [
    path('my_offers/', views.my_offers, name='my_offers'),
    path('messages/', views.messages, name='messages'),
    path('email_user/<int:id>/', views.email_user, name='email_user'),
    path('make_offer/<int:id>/', views.make_offer, name='make_offer'),
    path('offers_on_design/<int:id>/', views.offers_on_design, name='offers_on_design'),
    path('delete_message/', views.delete_message, name='delete_message'),
    path('delete_offer/', views.delete_offer, name='delete_offer'),
]
