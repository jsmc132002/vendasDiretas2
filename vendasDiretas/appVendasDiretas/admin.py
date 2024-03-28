from django.contrib import admin
from appVendasDiretas.models import Fornecedor, Produto, Cliente, Pedido

# Register your models here.
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Pedido)