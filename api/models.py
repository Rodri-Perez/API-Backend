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


class Usuarios(models.Model):
    Id_Usuario = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)


# [{nombre: pesa, precio:500, cant:2}, {nombre: pelota, precio:500, cant:2}]
class Compras(models.Model):

    Id_Compra = models.AutoField(primary_key=True),
    Cantidad = models.CharField(max_length=10),
    Fecha_Compra = models.DateField()


class Metodo_Pago(models.Model):
    Visa = models.CharField(max_length=255),
    Nro_de_tarjeta = models.CharField(max_length=16),
    Nro_de_seguridad = models.CharField(max_length=3),
    Titular_de_la_tarjeta = models.CharField(max_length=255),
    Fecha_de_vencimiento = models.CharField(max_length=5)
