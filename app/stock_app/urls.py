from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import importar_produtos, VendedorViewSet, CompradorViewSet, ProdutoViewSet, VendaViewSet, CompraViewSet, EstoqueViewSet

router = DefaultRouter()
router.register(r'vendedores', VendedorViewSet)
router.register(r'compradores', CompradorViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'compras', CompraViewSet)
router.register(r'estoques', EstoqueViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('importar-produtos/', importar_produtos, name='importar-produtos'),
]
