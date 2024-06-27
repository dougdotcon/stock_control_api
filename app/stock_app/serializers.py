from rest_framework import serializers
from .models import Vendedor, Comprador, Produto, Venda, Compra, Estoque

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['id', 'nome', 'email']

class CompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprador
        fields = ['id', 'nome', 'email']
        
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'quantidade_estoque']

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ['id', 'produto', 'vendedor', 'comprador', 'quantidade', 'data', 'preco_final']

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['id', 'produto', 'comprador', 'quantidade', 'data', 'preco_final']

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = ['id', 'produto', 'quantidade']
