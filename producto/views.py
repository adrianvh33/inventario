from ast import mod
from multiprocessing import context
from pyexpat import model
from re import template
from attr import fields
from django.shortcuts import render
from django.http import Http404
from .models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,ListView,CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import ProductosForms
import datetime
# Create your views here.



class ProductosDeleteView(LoginRequiredMixin,DeleteView):
    model = Producto
    success_url = '/productos'
    template_name = 'productos/productos_delete.html'
    login_url = '/'


class ProductosUpdateView(LoginRequiredMixin,UpdateView):
    model= Producto
    template_name = 'productos/productos_form.html'
    success_url = '/productos'
    form_class = ProductosForms
    login_url = '/'
    
    def form_valid(self, form):
        form.instance.editado = datetime.datetime.now()
        return super().form_valid(form)


class ProductosCreateView(LoginRequiredMixin,CreateView):
    model= Producto
    template_name = 'productos/productos_form.html'
    success_url = '/productos'
    form_class = ProductosForms
    login_url = '/'
    
    def form_valid(self, form):
        form.instance.editado = datetime.datetime.now()
        return super().form_valid(form)

class ProductosListView(LoginRequiredMixin,ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'productos/productos_list.html'
    login_url = '/'


class ProductoDetailView(LoginRequiredMixin,DetailView):
    model = Producto
    context_object_name ='producto'
    template_name = 'productos/producto_detalle.html'
    login_url = '/'