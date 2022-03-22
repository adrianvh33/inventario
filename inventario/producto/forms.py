import imp
from pyexpat import model
from tkinter import Widget
from attr import fields
import django


from django import forms
from .models import Producto

class ProductosForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('referencia','nombre','talla', 'sexo', 'precio', 'cantidad')
        widgets ={
            'referencia': forms.TextInput(attrs={'class':'form-control my-3'}),
            'nombre': forms.TextInput(attrs={'class':'form-control my-3'}),
            'talla': forms.TextInput(attrs={'class':'form-control my-3'}),
            'sexo': forms.TextInput(attrs={'class':'form-control my-3'}),
            'precio': forms.NumberInput(attrs={'class':'form-control my-3'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control my-3'}),
        }
        labels = {
            'sexo': 'Tipo'
        }
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 0:
            raise ValueError('La cantidad debe ser mayor a 0')
        return cantidad