from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from .models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,ListView,CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import ProductosForms
import datetime
from openpyxl import load_workbook

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

def importar(request):
    editado = datetime.datetime.now()
    if request.method == 'POST':
        file = request.FILES['doc']
        wb = load_workbook(file)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, min_col=1):
            referencia = row[0].value
            nombre = row[1].value
            nombre = nombre.split(' ')
            talla = nombre[-1]
            sexo = nombre[-2]
            nombre = ' '.join(nombre[:-2])
            cantidadSistema = row[2].value
            if row[3].value:
                precio = row[3].value
            else:
                precio = 0
            #print('nombre',nombre,'talla',talla,'tipo',sexo)
            Producto.objects.create(referencia=referencia,nombre=nombre,talla=talla,sexo=sexo,cantidadSistema=cantidadSistema,precio=precio,editado=editado)
        return HttpResponseRedirect(reverse('productos.list'))

    return render(request,'productos/importar.html', {})