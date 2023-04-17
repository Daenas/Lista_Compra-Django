from django.shortcuts import render
from .models import Produto
from django.http import HttpResponse

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso' : 'Programação com Django Framework',
        'outro' : 'Django é massa',
        'produtos' : produtos
    }

    return render(request, 'index.html', context)

def processa_formulario(request):
    produto = request.POST.get('produto')
    quantidade = request.POST.get('quantidade')

    context = {
        'produto' : produto,
        'quantidade' : quantidade
    }

    return render(request, 'processa_formulario.html', context)