from rest_framework import viewsets
from .serializer import ProductoSerializer, UsuarioSerializer
from .models import Producto, Usuarios


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer
