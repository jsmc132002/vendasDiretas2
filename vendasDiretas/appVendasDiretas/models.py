from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.nome + " " + self.fornecedor.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=264, unique=True)
    area = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.nome + " que trabalha com " + self.area

class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return self.produto + self.cliente + str(self.data)
