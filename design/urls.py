from django.urls import path
from . import views

urlpatterns = [
    path('design_list/', views.design_list, name='design_list'),
    path('propose_design/', views.propose_design, name='propose_design'),
    path('my_design/', views.my_design, name='my_design'),
]
