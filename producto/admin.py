from django.contrib import admin
from . import models
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('referencia','nombre','talla','cantidadSistema','cantidadContada','precio')

admin.site.register(models.Producto, ProductoAdmin)