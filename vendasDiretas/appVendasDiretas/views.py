from django.shortcuts import render
from django.http import HttpResponse
from appVendasDiretas.models import Fornecedor, Produto, Cliente, Pedido
from appVendasDiretas.forms import FornecedorForm, ProdutoForm, ClienteForm, PedidoForm

# Create your views here.
def index(request):
    listaFornecedores = Fornecedor.objects.order_by('nome')
    fornecedoresDict = {'registrosFornecedores': listaFornecedores}
    return render (request, 'appVendasDiretas/index.html', context=fornecedoresDict)

def cadastroFornecedor(request):
    form = FornecedorForm()

    if request.method == 'POST':
        form = FornecedorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Formulário inválido')

    return render(request, 'appVendasDiretas/formFornecedor.html',{'form':form})

def cadastroProduto(request):
    form = ProdutoForm()
    return render(request, 'appVendasDiretas/formProduto.html',{'form':form})

def cadastroCliente(request):
    form = ClienteForm()
    return render(request, 'appVendasDiretas/formCliente.html',{'form':form})

def cadastroPedido(request):
    form = PedidoForm()
    return render(request, 'appVendasDiretas/formPedido.html',{'form':form})