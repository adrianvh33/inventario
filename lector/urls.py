from django.urls import path
from . import views


urlpatterns = [
    path('leer', views.leer,name='lector.leer'),
]