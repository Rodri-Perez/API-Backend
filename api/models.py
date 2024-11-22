from django.db import models
from uuid import *
from django.core.validators import MinValueValidator, MaxValueValidator


class Producto(models.Model):

    id_producto = models.AutoField(primary_key=True)
    cod = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    talle_peso = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()

 # INVERTIR LAS UUID DE PRODUCTO A USUARIO YT BICEVERSA
 # AHILITAR BUSQUEDA PARA CAMPOS UNICOS


class Usuarios(models.Model):
    Id_Usuario = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    Username = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)


class MetodoPago(models.Model):

    id_pago = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255)


class Compras(models.Model):

    Id_Compra = models.AutoField(primary_key=True)
    Id_user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(default=0)
    Id_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Fecha_Compra = models.DateField()
    id_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)


class Tarjetas(models.Model):
    id_tarjetas = models.UUIDField(
        primary_key=True, editable=False)
    Visa = models.CharField(max_length=255, default=0)
    Nro_de_tarjeta = models.CharField(max_length=16, default=0)
    Nro_de_seguridad = models.CharField(max_length=3, default=0)
    Id_user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Fecha_de_vencimiento = models.CharField(max_length=5)
