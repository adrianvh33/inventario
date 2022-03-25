from django.shortcuts import render
from .forms import LeerForm
from producto.models import Producto
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.
def leer(request):
    if request.method == 'POST':
        filled_form = LeerForm(request.POST)
        if filled_form.is_valid():
            referencia = filled_form.cleaned_data['referencia']
            print(referencia)
            if Producto.objects.filter(referencia=referencia).exists():
                prod = Producto.objects.get(referencia=referencia)
                prod.enTienda = prod.enTienda
                prod.save()
            note = 'Cantidad contada de {} - {} es {}'.format(prod.referencia,prod.nombre,prod.enTienda)    
            form = LeerForm()
            return render(request,'lector/leer.html', {'form':form, 'note':note})
    else:
        form = LeerForm()
        return render(request,'lector/leer.html', {'form':form})