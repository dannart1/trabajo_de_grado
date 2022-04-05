from django.urls import path
from . import views
from django.views.static import serve

urlpatterns = [
    path('', views.set_temperatura, name='set_temperatura'),
    path('set_humedad/', views.set_humedad, name='set_humedad'),
    path('set_conteo/', views.set_conteo, name='set_conteo'),
    path('set_deteccion/', views.set_deteccion, name='set_deteccion'),
    path('set_about/', views.set_about, name='set_about'),
    path('set_script/', views.set_about, name='set_script'),
]