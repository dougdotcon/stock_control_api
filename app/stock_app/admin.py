from django.contrib import admin
from .models import Vendedor, Comprador, Produto, Venda, Compra, Estoque

admin.site.register(Vendedor)
admin.site.register(Comprador)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Compra)
admin.site.register(Estoque)
