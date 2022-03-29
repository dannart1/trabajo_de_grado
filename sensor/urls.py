from django.urls import path
from . import views
from django.views.static import serve

urlpatterns = [
    path('', views.post_values, name='post_values'),
    #path(r'^Graficador/$', views.Graficador),
]