from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200,unique=True)
    precio = models.DecimalField(default=0,max_digits=10, decimal_places=2)
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
    diferencia= models.IntegerField(
        default=0,
     )
    editado = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.diferencia = (self.enTienda + self.enBloque5 + self.enBloque2) - self.cantidadSistema 
        return super(Producto, self).save()