from django import forms
from django.core import validators
from appVendasDiretas.models import Fornecedor, Produto, Cliente, Ciclo, Pedido, DetalheDoPedido
import datetime

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        #fields = '__all__'
        fields = ('nome', 'cnpj', 'telefone', 'site', 'email')
        widgets = {
            'nome': forms.TextInput(attrs={'class': "form-control"}),
            'cnpj': forms.TextInput(attrs={'class': "form-control"}),
            'telefone': forms.TextInput(attrs={'class': "form-control"}),
            'site': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
        }



class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('fornecedor', 'codigo', 'nome', 'valor')
        widgets = {
            'fornecedor': forms.Select(attrs={'class': "form-control"}),
            'codigo': forms.TextInput(attrs={'class': "form-control"}),
            'nome': forms.TextInput(attrs={'class': "form-control"}),
            'valor': forms.TextInput(attrs={'class': "form-control"}),
        }
    


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'alias', 'telefone', 'email')
        widgets = {
            'nome': forms.TextInput(attrs={'class': "form-control"}),
            'alias': forms.TextInput(attrs={'class': "form-control"}),
            'telefone': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
        }
        


class CicloForm(forms.ModelForm):
    class Meta:
        model = Ciclo
        fields = ('fornecedor', 'ciclo', 'dataInicio', 'dataFim',)
        widgets = {
            'fornecedor': forms.Select(attrs={'class': "form-control"}),
            'ciclo': forms.TextInput(attrs={'class': "form-control"}),
            'dataInicio': forms.TextInput(attrs={'class': "form-control"}),
            'dataFim': forms.TextInput(attrs={'class': "form-control"}),
        }



class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('ciclo', 'cliente', 'data',)
        widgets = {
            'ciclo': forms.Select(attrs={'class': "form-control"}),
            'cliente': forms.Select(attrs={'class': "form-control"}),
            'data': forms.TextInput(attrs={'class': "form-control"}),
        }



class DetalheDoPedidoForm(forms.ModelForm):
    class Meta:
        model = DetalheDoPedido
        fields = ('idPedido', 'produto', 'quantidade', )
        widgets = {
            'idPedido': forms.Select(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.TextInput(attrs={'class': 'form-control'}),
        }