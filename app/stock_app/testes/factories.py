import factory
from factory.django import DjangoModelFactory
from ..models import Vendedor, Produto, Venda

class VendedorFactory(DjangoModelFactory):
    class Meta:
        model = Vendedor
    
    nome = factory.Faker('name')
    email = factory.Faker('email')

class ProdutoFactory(DjangoModelFactory):
    class Meta:
        model = Produto
    
    nome = factory.Faker('word')
    preco = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    estoque = factory.Faker('pyint', min_value=1, max_value=100)

class VendaFactory(DjangoModelFactory):
    class Meta:
        model = Venda
    
    vendedor = factory.SubFactory(VendedorFactory)
    produto = factory.SubFactory(ProdutoFactory)
    quantidade = factory.Faker('pyint', min_value=1, max_value=20)
    data = factory.Faker('date')
