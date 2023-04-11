from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso' : 'Programação com Django Framework',
        'outro' : 'Django é massa',
        'produtos' : produtos
    }

    return render(request, 'index.html', context)

