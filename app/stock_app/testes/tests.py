from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from ..models import Vendedor, Produto, Venda
from .factories import VendedorFactory, ProdutoFactory, VendaFactory
from stock_app.serializers import ProdutoSerializer

class VendedorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendedor = VendedorFactory()

    def test_create_vendedor(self):
        url = reverse('vendedor-list')
        data = {'nome': 'João Silva', 'email': 'joao@exemplo.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_vendedor_detail(self):
        url = reverse('vendedor-detail', args=[self.vendedor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_vendedor(self):
        url = reverse('vendedor-detail', args=[self.vendedor.id])
        data = {'nome': 'João Santos'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_vendedor(self):
        url = reverse('vendedor-detail', args=[self.vendedor.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ReportEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.venda = VendaFactory()

    def test_pdf_report_generation(self):
        url = reverse('venda-report', args=['pdf'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_excel_report_generation(self):
        url = reverse('venda-report', args=['excel'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

class VendaTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.venda = VendaFactory()

    def test_create_venda(self):
        vendedor = VendedorFactory()
        produto = ProdutoFactory()
        url = reverse('venda-list')
        data = {'vendedor': vendedor.id, 'produto': produto.id, 'quantidade': 5}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_venda_detail(self):
        url = reverse('venda-detail', args=[self.venda.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ProdutoSerializerTests(TestCase):
    def test_valid_produto_data(self):
        valid_data = {'nome': 'Produto Teste', 'preco': 10.00, 'estoque': 15}
        serializer = ProdutoSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_produto_data(self):
        invalid_data = {'nome': '', 'preco': -20, 'estoque': -1}
        serializer = ProdutoSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
