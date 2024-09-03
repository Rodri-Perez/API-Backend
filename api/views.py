from rest_framework import viewsets, generics, authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .serializer import ProductoSerializer, ProductoSerializer,  AuthTokenSerializer
from .models import Producto


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CreateProductoView(generics.CreateAPIView):
    serializer_class = productoSerializer

class RetreiIveUpdateProdictoView(generics.RetrieveUpdateAPIView):
    serializer_class = ProductoSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        queryset = Producto.objects.all()
        serializer_class = ProductoSerializer
        return self.request.ProductoViewSet


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer