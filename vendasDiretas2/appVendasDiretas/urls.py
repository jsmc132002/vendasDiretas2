from appVendasDiretas import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path("cadastroFornecedor", views.cadastroFornecedor, name='cadadstroFornecedor'),
]
