from turtle import onclick
from django import forms

class LeerForm(forms.Form):
    CHOICES=[('tienda','Tienda'),
         ('bloque2','Bloque 2'),
         ('bloque5','Bloque 5') ]

    referencia = forms.CharField(label='Escriba la referencia',widget=forms.TextInput(attrs={'id':'refe', 'autofocus': 'autofocus'}))
    ubicacion = forms.ChoiceField(choices=CHOICES,label='Escoja la ubicacion', widget=forms.RadioSelect(attrs={'id':'radio', 'class':'my-2'}))
    
