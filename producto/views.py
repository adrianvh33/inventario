from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.urls import is_valid_path, reverse
from .models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,ListView,CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import ProductosForms, ImportarForm, ContadorForm
import datetime
from openpyxl import load_workbook
from django.db import transaction
from django.views.generic.edit import FormMixin
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
    productos = []

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(referencia=query)
        return qs


class ProductoDetailView(LoginRequiredMixin,UpdateView):
    model = Producto
    template_name = 'productos/producto_detalle.html'
    success_url = '/productos'
    form_class = ContadorForm
    login_url = '/'

    def form_valid(self, form):
        form.save()
        return super(ProductoDetailView, self).form_valid(form)


def importar(request):
    editado = datetime.datetime.now()
    if request.method == 'POST':
        filled_form = ImportarForm(request.POST, request.FILES)
        if filled_form.is_valid():
            file = request.FILES['file']
            wb = load_workbook(file)
            sheet = wb.active
            with transaction.atomic():
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
                    
                    if Producto.objects.filter(referencia=referencia).exists():
                        prod = Producto.objects.get(referencia=referencia)
                        prod.cantidadSistema=cantidadSistema
                        prod.save()
                    else:
                        Producto.objects.create(referencia=referencia,nombre=nombre,talla=talla,sexo=sexo,cantidadSistema=cantidadSistema,precio=precio,editado=editado)
            return HttpResponseRedirect(reverse('productos.list'))
        else:
            form = ImportarForm()
            print(filled_form.errors)
    else:
        form = ImportarForm()
    return render(request,'productos/importar.html', {'form':form})