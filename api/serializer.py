from rest_framework import serializers
from .models import Producto, Usuarios, Compras, Tarjetas, MetodoPago


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'


class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = '__all__'


class TarjetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjetas
        fields = '__all__'


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'
