from venv import create
from django.db import models

class Inventarios(models.Model):
    nombre = models.CharField(max_length=200)
    creado = models.DateField(auto_now_add=True)
    