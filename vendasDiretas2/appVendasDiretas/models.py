from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    idFornecedor = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=264, unique=True)
    cnpj = models.CharField(max_length=264, blank=True)
    telefone = models.CharField(max_length=264, blank=True)
    site = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.nome
    


class Ciclo(models.Model):
    idCiclo = models.BigAutoField(primary_key=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    ciclo = models.CharField(max_length=264, unique=True)
    dataInicio = models.DateField(default=0)
    dataFim = models.DateField(default=0)

    def __str__(self):
        return self.ciclo
    


class Produto(models.Model):
    idProduto = models.BigAutoField(primary_key=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=264, )
    nome = models.CharField(max_length=264, )
    valor = models.DecimalField(max_digits=13, decimal_places=2)

    def __str__(self):
        return self.nome



class Cliente(models.Model):
    idCliente = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=264)
    alias = models.CharField(max_length=264, unique=True)
    telefone = models.CharField(max_length=12)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.alias



class Pedido(models.Model):
    idPedido = models.BigAutoField(primary_key=True)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.CharField(max_length=264)

    def __str__(self):
        return str(self.idPedido)



class DetalheDoPedido(models.Model):
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
