from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import ProductoSerializer, UsuarioSerializer, ComprasSerializer, TarjetasSerializer
from .models import Producto, Usuarios, Compras, Tarjetas


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Email']


class ComprasViewSet(viewsets.ModelViewSet):
    queryset = Compras.objects.all()
    serializer_class = ComprasSerializer


class TarjetasViewSet(viewsets.ModelViewSet):
    queryset = Tarjetas.objects.all()
    serializer_class = TarjetasSerializer
