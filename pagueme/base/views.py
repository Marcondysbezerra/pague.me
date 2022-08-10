from django.shortcuts import render, redirect
from pagueme.base.forms import CriarUsuarioForm
from pagueme.base.models import Usuario
from django.core.paginator import Paginator


def lista(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Usuario.objects.filter(nome__icontains=search)
    else:
        data['db'] = Usuario.objects.all()
    #all = Usuario.objects.all()
    #paginator = Paginator(all, 8)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'base/lista_de_clientes.html', data)


def paginator(request):
    data = {}
    #data['db'] = Usuario.objects.all()
    all = Usuario.objects.all()
    paginator = Paginator(all, 8)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'base/lista_de_clientes.html', data)


def form(request):
    data = {}
    data['form'] = CriarUsuarioForm()
    return render(request, 'base/cadastro.html', data)


def create(request):
    form = CriarUsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista')


def view(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    return render(request, 'base/detalhe.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    data['form'] = CriarUsuarioForm(instance=data['db'])
    return render(request, 'base/cadastro.html', data)


def update(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    form = CriarUsuarioForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('lista')


def delete(request, pk):
    db = Usuario.objects.get(pk=pk)
    db.delete()
    return redirect('lista')