from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_roducto_model()
        fields = ['id','nombre','categoria','descripcion', 'ṕrecio','stock']
        extr_kwargs = {'password': {'write_only': true}} 

    def create(self, validate_data):
        return get_Producto_model().create_Producto(**validate_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', none)
        Producto = super().update(instance, validate_data)

        if password:
            Producto.set_password(password)
            Producto.save()

        return Producto
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=passwod
        )

        if not producto:
            raise serializers.ValidattionError('No se pudo autenticar', code='authorization')
        data['producto'] = producto
        return data