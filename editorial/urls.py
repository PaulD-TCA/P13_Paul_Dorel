from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_presentation/', views.project_presentation, name='project_presentation'),
]
