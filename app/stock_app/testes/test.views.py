from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from .factories import ProdutoFactory, VendaFactory

class ProdutoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.produto = ProdutoFactory()

    def test_create_produto(self):
        url = reverse('produto-list')
        data = {'nome': 'Novo Produto', 'preco': 50.00, 'estoque': 100}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], 'Novo Produto')

    def test_read_produto_list(self):
        url = reverse('produto-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Novo Produto', [item['nome'] for item in response.data])

    def test_read_produto_detail(self):
        url = reverse('produto-detail', args=[self.produto.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.produto.nome)

    def test_update_produto(self):
        url = reverse('produto-detail', args=[self.produto.id])
        data = {'nome': 'Produto Atualizado', 'preco': 55.00}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Produto Atualizado')

    def test_delete_produto(self):
        url = reverse('produto-detail', args=[self.produto.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_data_create(self):
        url = reverse('produto-list')
        data = {'nome': '', 'preco': -10, 'estoque': -1}  
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class TestProcessoDeCompra(TestCase):
    def test_processo_de_compra_reduz_estoque(self):
        produto = ProdutoFactory(estoque=100)
        VendaFactory(produto=produto, quantidade=10)
        produto.refresh_from_db()
        self.assertEqual(produto.estoque, 90)