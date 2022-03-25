# Generated by Django 4.0.3 on 2022-03-25 13:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_remove_producto_sexo_remove_producto_talla'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='cantidadContada',
            new_name='enBloque2',
        ),
        migrations.AddField(
            model_name='producto',
            name='enBloque5',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='producto',
            name='enTienda',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]