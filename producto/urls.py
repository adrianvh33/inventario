from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.ProductosListView.as_view(), name='productos.list'),
    path('productos/<int:pk>', views.ProductoDetailView.as_view(),name='productos.detail'),
    path('productos/nuevo', views.ProductosCreateView.as_view(),name='productos.new'),
    path('productos/<int:pk>/editar', views.ProductosUpdateView.as_view(),name='productos.update'),
    path('productos/<int:pk>/eliminar', views.ProductosDeleteView.as_view(),name='productos.delete'),
    path('productos/importar', views.importar,name='productos.importar'),
    path('productos/reporte', views.reporte,name='productos.reporte'),
    path('productos/eliminarTodo', views.deleteAll,name='productos.deleteAll'),
]