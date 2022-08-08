from django.shortcuts import render, redirect

# Create your views here.
from pagueme.base.forms import CriarUsuario
from pagueme.base.models import Usuario


def lista_de_clientes(request):
    clientes = Usuario.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'base/lista_de_clientes.html', context=context)


def cadastro(request):
    usuario = CriarUsuario()
    if request.method == 'POST':
        usuario = CriarUsuario(request.POST)
        if usuario.is_valid():
            usuario.save()
            print(request)
            return redirect('/lista/')
        else:
            return render(request, 'base/cadastro.html')
    else:
        return render(request, 'base/cadastro.html')


def detalhe(request):
    return render(request, 'base/detalhe.html')
