from django.shortcuts import render
from .forms import LeerForm
from producto.models import Producto
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.

def leerList(request):
    return render(request,'lector/lector_list.html', {})


def leerTienda(request):
    if request.method == 'POST':
        filled_form = LeerForm(request.POST)
        if filled_form.is_valid():
            referencia = filled_form.cleaned_data['referencia']
            print(referencia)
            if Producto.objects.filter(referencia=referencia).exists():
                prod = Producto.objects.get(referencia=referencia)
                prod.enTienda = prod.enTienda + 1
                prod.save()
            note = 'Cantidad en Tienda de {} - {} es {}'.format(prod.referencia,prod.nombre,prod.enTienda)    
            form = LeerForm()
            return render(request,'lector/leer.html', {'form':form, 'note':note})
    else:
        form = LeerForm()
        return render(request,'lector/leer.html', {'form':form})

def leerBloque2(request):
    if request.method == 'POST':
        filled_form = LeerForm(request.POST)
        if filled_form.is_valid():
            referencia = filled_form.cleaned_data['referencia']
            print(referencia)
            if Producto.objects.filter(referencia=referencia).exists():
                prod = Producto.objects.get(referencia=referencia)
                prod.enBloque2 = prod.enBloque2 + 1
                prod.save()
            note = 'Cantidad en bloque 2 de {} - {} es {}'.format(prod.referencia,prod.nombre,prod.enBloque2)    
            form = LeerForm()
            return render(request,'lector/leer.html', {'form':form, 'note':note})
    else:
        form = LeerForm()
        return render(request,'lector/leer.html', {'form':form})

def leerBloque5(request):
    if request.method == 'POST':
        filled_form = LeerForm(request.POST)
        if filled_form.is_valid():
            referencia = filled_form.cleaned_data['referencia']
            print(referencia)
            if Producto.objects.filter(referencia=referencia).exists():
                prod = Producto.objects.get(referencia=referencia)
                prod.enBloque5 = prod.enBloque5 + 1
                prod.save()
            note = 'Cantidad en bloque 5 de {} - {} es {}'.format(prod.referencia,prod.nombre,prod.enBloque5)    
            form = LeerForm()
            return render(request,'lector/leer.html', {'form':form, 'note':note})
    else:
        form = LeerForm()
        return render(request,'lector/leer.html', {'form':form})