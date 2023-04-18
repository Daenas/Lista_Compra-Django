from django.shortcuts import render
from .models import Produto
from .forms import ProdutoModelForm

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso' : 'Programação com Django Framework',
        'outro' : 'Django é massa',
        'produtos' : produtos
    }

    return render(request, 'index.html', context)

def processa_formulario(request):
    Nome = request.POST.get('produto')
    Quantidade = request.POST.get('quantidade')

    context = {
        'Nome' : Nome,
        'Quantidade' : Quantidade
    }

    return render(request, 'processa_formulario.html', context)