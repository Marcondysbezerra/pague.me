from django.urls import path
from pagueme.base.views import lista_de_clientes, cadastro, detalhe

urlpatterns = [
    path('', lista_de_clientes, name='lista'),
    path('cadastro/', cadastro, name='cadastro'),
    path('detalhe/', detalhe, name='detalhe'),
]
