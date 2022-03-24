from django.shortcuts import render
from .forms import LeerForm
# Create your views here.
def leer(request):
    if request.method == 'POST':
        filled_form = LeerForm(request.POST)
        if filled_form.is_valid():
            referencia = filled_form.referencia
            print(referencia)
            form = LeerForm()
    else:
        form = LeerForm()
    return render(request,'lector/leer.html', {'form':form})