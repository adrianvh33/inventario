from django.contrib import admin
from . import models
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('referencia','nombre','cantidadSistema','enTienda','enBloque2','enBloque5','precio')

admin.site.register(models.Producto, ProductoAdmin)