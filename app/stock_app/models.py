from django.db import models

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Comprador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='estoque_record')
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"

class Venda(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Comprador, on_delete=models.SET_NULL, null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_final = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda de {self.quantidade}x {self.produto.nome} em {self.data.strftime('%Y-%m-%d %H:%M')}"

class Compra(models.Model):
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_final = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compra de {self.quantidade}x {self.produto.nome} em {self.data.strftime('%Y-%m-%d %H:%M')}"
