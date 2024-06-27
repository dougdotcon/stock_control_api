import requests
from rest_framework import viewsets
from .models import Vendedor, Comprador, Produto, Venda, Compra, Estoque
from .serializers import VendedorSerializer, CompradorSerializer, ProdutoSerializer, VendaSerializer, CompraSerializer, EstoqueSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Venda, Produto
from .reports import generate_pdf_report, generate_excel_report

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class CompradorViewSet(viewsets.ModelViewSet):
    queryset = Comprador.objects.all()
    serializer_class = CompradorSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    def perform_create(self, serializer):
        produto = serializer.validated_data['produto']
        quantidade = serializer.validated_data['quantidade']
        preco_final = serializer.validated_data.get('preco_final', produto.preco * quantidade) 
        serializer.save(preco_final=preco_final)

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def perform_create(self, serializer):
        produto = serializer.validated_data['produto']
        quantidade = serializer.validated_data['quantidade']
        preco_final = serializer.validated_data.get('preco_final', produto.preco * quantidade)  
        serializer.save(preco_final=preco_final)
        
class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data', 'vendedor__nome', 'comprador__nome']

    @action(detail=False, methods=['get'], url_path='report-(?P<format_type>pdf|excel)')
    def sales_report(self, request, format_type=None):
        if format_type == 'pdf':
            return generate_pdf_report(self.filter_queryset(self.get_queryset()))
        elif format_type == 'excel':
            return generate_excel_report(self.filter_queryset(self.get_queryset()))
        else:
            return Response({"error": "Format not supported"}, status=400)
        
@api_view(['GET'])
def importar_produtos(request):
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    produtos = response.json()
    for produto in produtos:
        Produto.objects.create(
            nome=produto['title'],
            preco=produto['price'],
            quantidade_estoque=10 
        )
    return Response({'status': 'Produtos importados com sucesso!'})