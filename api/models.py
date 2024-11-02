from django.db import models


class Producto(models.Model):

    id_producto = models.UUIDField(
        primary_key=True, editable=False),
    cod = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    talle_peso = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()
