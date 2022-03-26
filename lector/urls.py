from django.urls import path
from . import views


urlpatterns = [
    path('lector', views.lector,name='lector.lector'),
]