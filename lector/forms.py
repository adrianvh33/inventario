from django import forms

class LeerForm(forms.Form):
    referencia = forms.CharField(label='Escriba la referencia',widget=forms.TextInput(attrs={'id':'refe', 'class':''}))