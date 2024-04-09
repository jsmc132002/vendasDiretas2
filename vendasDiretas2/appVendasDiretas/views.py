from django.shortcuts import render
from django.http import HttpResponse
from appVendasDiretas.models import Fornecedor, Produto, Cliente, Pedido
from appVendasDiretas.forms import FornecedorForm, ProdutoForm, ClienteForm, PedidoForm, CicloForm, DetalheDoPedidoForm

# Create your views here.
def index(request):
    listaFornecedores = Fornecedor.objects.order_by('nome')
    fornecedoresDict = {'registrosFornecedores': listaFornecedores}

    return render (request, 'appVendasDiretas/index.html', context=fornecedoresDict)



def listaDeFornecedores(request):
    listaFornecedores = Fornecedor.objects.order_by('nome')
    fornecedoresDict = {'registrosFornecedores': listaFornecedores}
    for x in fornecedoresDict:
        print(fornecedoresDict)

    return fornecedoresDict



def cadastroFornecedor(request):
    form = FornecedorForm()
    if request.method == 'POST':
        form = FornecedorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Formulário fornecedor inválido')

    return render(request, 'appVendasDiretas/formCadastroFornecedor.html',{'form':form})



def cadastroProduto(request):
    form = ProdutoForm()
    if request.method =='POST':
        form = ProdutoForm(request.POST)
    
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Formulário produto inválido')
 
    return render(request, 'appVendasDiretas/formCadastroProduto.html',{'form':form})



def cadastroCliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Formulário cliente inválido')    

    return render(request, 'appVendasDiretas/formCadastroCliente.html',{'form':form})



def cadastroCiclo(request):
    form = CicloForm()
    if request.method == 'POST':
        form = CicloForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Formulário ciclo inválido')

    return render(request, 'appVendasDiretas/formCadastroCiclo.html',{'form':form})



def cadastroPedido(request):
    form = PedidoForm()
    if request.method == 'POST':
        form = PedidoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Formulário pedido inválido')

    return render(request, 'appVendasDiretas/formCadastroPedido.html',{'form':form})


def cadastroDetalheDoPedido(request):
    form = DetalheDoPedidoForm()
    if request.method == 'POST':
        form = DetalheDoPedidoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Formulário Detalhe do pedido inválido')   

    return render(request, 'appVendasDiretas/formCadastroDetalheDoPedido.html',{'form':form})



