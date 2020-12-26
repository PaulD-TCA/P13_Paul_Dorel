from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('design_list/', views.design_list, name='design_list'),
    path('upload_design/', views.upload_design, name='upload_design'),
    path('my_design/', views.my_design, name='my_design'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
