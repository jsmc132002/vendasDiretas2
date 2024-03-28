from django import forms
from django.core import validators
from appVendasDiretas.models import Fornecedor

#Não está conectado ao Model
#class FornecedorForm(forms.Form):
#    Nome = forms.CharField()
#    Email = forms.EmailField()
#    Observacao = forms.CharField(widget=forms.Textarea)
#    botCatcher = forms.CharField(required=False, 
#                                 widget=forms.HiddenInput,
#                                validators=[validators.MaxLengthValidator(0)])

#carrega direto do Model
class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'


#Não está conectato ao Model
class ProdutoForm(forms.Form):
    Codigo = forms.IntegerField()
    Nome = forms.CharField()
    

class ClienteForm(forms.Form):
    Nome = forms.CharField()
    Email = forms.EmailField()
    Telefone = forms.CharField()


class PedidoForm(forms.Form):
    Cliente = forms.CharField()
    Codigo = forms.CharField()
    Produto = forms.CharField()
    Quantidade = forms.CharField()
    Observações = forms.CharField(widget=forms.Textarea)

