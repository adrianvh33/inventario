
from .models import Inventarios
from django import forms
class InventariosForms(forms.ModelForm):
    class Meta:
        model = Inventarios
        fields = ('nombre',)
        widgets ={
            'nombre': forms.TextInput(attrs={'class':'form-control my-3'}),
        }
        