from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViewSet)
router.register(r'usuarios', views.UsuariosViewSet)
router.register(r'compras', views.ComprasViewSet)
router.register(r'tarjetas', views.TarjetasViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls))


]
