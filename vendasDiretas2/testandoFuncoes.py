
from appVendasDiretas.models import Fornecedor

def listaforne():
    listaFornecedores = Fornecedor.objects.order_by('nome')
    fornecedoresDict = {'registrosFornecedores': listaFornecedores}
    for x in fornecedoresDict:
        print(fornecedoresDict)

    return fornecedoresDict