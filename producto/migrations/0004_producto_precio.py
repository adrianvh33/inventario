# Generated by Django 4.0.3 on 2022-03-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_alter_producto_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=20000, max_digits=10),
            preserve_default=False,
        ),
    ]