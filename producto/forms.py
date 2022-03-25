from asyncio import coroutines
import django

from django import forms
from .models import Producto

class ProductosForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('referencia','nombre', 'precio', 'cantidadSistema','enTienda','enBloque2','enBloque5')
        widgets ={
            'referencia': forms.TextInput(attrs={'class':'form-control my-3'}),
            'nombre': forms.TextInput(attrs={'class':'form-control my-3'}),
            'precio': forms.NumberInput(attrs={'class':'form-control my-3'}),
            'cantidadSistema': forms.NumberInput(attrs={'class':'form-control my-3'}),
            'enTienda': forms.NumberInput(attrs={'class':'form-control my-3'}),
            'enBloque2': forms.NumberInput(attrs={'class':'form-control my-3'}),
            'enBloque5': forms.NumberInput(attrs={'class':'form-control my-3'}),
        }
        labels = {
            'enTienda': 'Cantidad en tienda',
            'enBloque2': 'Cantidad en Bloque 2',
            'enBloque5': 'Cantidad en Bloque 5'
        }
        
    def clean_cantidad(self):
        enTienda = self.cleaned_data['enTienda']
        if enTienda < 0:
            raise ValueError('La cantidad debe ser mayor a 0')
        return enTienda

class ImportarForm(forms.Form):
    file = forms.FileField(label='Subir archivo')

class ContadorForm(forms.ModelForm):
    CHOICES=[('tienda','Tienda'),
         ('bloque2','Bloque 2'),
         ('bloque5','Bloque 5') ]
    radioTienda = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id':'radio', 'class':'','onclick':'EnableDisableTB()'}))
    class Meta:
        model = Producto
        fields = ( 'enTienda','enBloque2','enBloque5')
        
        widgets ={
            'enTienda': forms.NumberInput(attrs={'class':'text-center', 'id':'counter-display1'}),
            'enBloque2': forms.NumberInput(attrs={'class':'text-center', 'id':'counter-display2'}),
            'enBloque5': forms.NumberInput(attrs={'class':'text-center', 'id':'counter-display3'}),
        }
        labels = {
            'enTienda': '',
            'enBloque2': '',
            'enBloque5': ''
        }