from ast import In
from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator
from inventario.models import Inventarios
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidadSistema = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
     )
    enTienda= models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
     )

    enBloque2= models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
     )
    
    enBloque5= models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
     )
    editado = models.DateTimeField()
    inventario = models.ForeignKey(Inventarios,on_delete=models.CASCADE, related_name="productos")