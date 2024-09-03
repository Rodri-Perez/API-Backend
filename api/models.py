from django.db import models


class Usuarios (models.Models):
    Id_Usuario = models.AutoField(primary_key=True, editable=False),
    Username = models.CharField(max_length=255),
    Email = models.EmailField(max_legth=255, primary_key=True),
    Password = models.CharField(max_legth=255)

    def __str__ (self):
        return self.Id_Usuario


# [{nombre: pesa, precio:500, cant:2}, {nombre: pelota, precio:500, cant:2}]
class Compras(models.Model):

    Id_Compra = models.AutoField(primary_key=True),
    Cantidad = models.CharField(max_length=10),
    Fecha_Compra = models.DateField()


class Productos(models.Model):

    Id_Producto = models.UUIDField(
        primary_key=True, editable=False),
    Categoria = models.CharField(max_length=255),
    Talle_peso = models.CharField(max_length=50),
    Descripcion = models.CharField(max_length=255),
    Stock = models.PositiveIntegerField(),

    def __str__(self):
        return self.Nombre


class Metodo_Pago(models.Model):
    Visa = models.CharField(max_length=255),
    Nro_de_tarjeta = models.CharField(max_length=16),
    Nro_de_seguridad = models.CharField(max_length=3),
    Titular_de_la_tarjeta = models.CharField(max_length=255),
    Fecha_de_vencimiento = models.CharField(max_length=5)

