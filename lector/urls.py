from django.urls import path
from . import views


urlpatterns = [
    path('lector', views.leerList,name='lector.list'),
    path('lector/leerTienda', views.leerTienda,name='lector.leerTienda'),
    path('lector/barcodeTienda', views.barcodeTienda,name='lector.barcodeTienda'),
]