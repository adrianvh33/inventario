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
            ubicacion = filled_form.cleaned_data['ubicacion']
            if Producto.objects.filter(referencia=referencia).exists():
                    prod = Producto.objects.get(referencia=referencia)
                    if(ubicacion == 'tienda'):
                        prod.enTienda= prod.enTienda + 1
                        prod.save() 
                        cantidad = prod.enTienda
                    elif(ubicacion == 'bloque2'):
                        prod.enBloque2= prod.enBloque2 + 1
                        prod.save() 
                        cantidad = prod.enBloque2
                    elif(ubicacion == 'bloque5'):
                        prod.enBloque5= prod.enBloque5 + 1
                        prod.save() 
                        cantidad = prod.enBloque5                                                                                            
                    note = 'Cantidad en {} de {} - {} es {}'.format(ubicacion,prod.referencia,prod.nombre,cantidad)    
                    form = LeerForm()
                    return render(request,'lector/leer.html', {'form':form, 'note':note})
            else:
                note = 'La referencia {} no existe'.format(referencia)  
                form = LeerForm()
                return render(request,'lector/leer.html', {'form':form, 'note':note})
    else:
        form = LeerForm()
        return render(request,'lector/leer.html', {'form':form})

def barcodeTienda(request):
    if request.method == 'POST':
        filled_form = LeerForm(request.POST)
        if filled_form.is_valid():
            referencia = filled_form.cleaned_data['referencia']
            print(referencia)
            if Producto.objects.filter(referencia=referencia).exists():
                prod = Producto.objects.get(referencia=referencia)
                prod.enTienda= prod.enTienda + 1
                prod.save()
                note = 'Cantidad en tienda de {} - {} es {}'.format(prod.referencia,prod.nombre,prod.enTienda)    
                form = LeerForm()
                return render(request,'lector/barcode.html', {'form':form, 'note':note})
            else:
                note = 'La referencia {} no existe'.format(referencia)  
                form = LeerForm()
                return render(request,'lector/leer.html', {'form':form, 'note':note})
    else:
        form = LeerForm()
        return render(request,'lector/barcode.html', {'form':form})