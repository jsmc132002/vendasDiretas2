import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appVendasDiretas.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random 
from appVendasDiretas.models import Fornecedor, Produto, Cliente, Pedido
from faker import Faker

fakegen = Faker()
