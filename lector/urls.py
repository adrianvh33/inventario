from django.urls import path
from . import views


urlpatterns = [
    path('lector', views.leerList,name='lector.list'),
    path('lector/leerTienda', views.leerTienda,name='lector.leerTienda'),
    path('lector/leerBloque2', views.leerBloque2,name='lector.leerBloque2'),
    path('lector/leerBloque5', views.leerBloque5,name='lector.leerBloque5'),
]