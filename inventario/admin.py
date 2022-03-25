from django.contrib import admin
from . import models
# Register your models here.
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    pass

admin.site.register(models.Inventarios, InventarioAdmin)