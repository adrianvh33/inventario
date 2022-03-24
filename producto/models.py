from pyexpat import model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    cantidadContada= models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
     )
    editado = models.DateTimeField()