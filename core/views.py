from django.shortcuts import render
from .models import Produto
from .forms import ProdutoModelForm
from django.contrib import messages

def index(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Produto salvo com sucesso!")
            form = ProdutoModelForm()
        else:
            messages.error(request, "Erro ao cadastrar produto.")
    else:
        form = ProdutoModelForm()

    produtos = Produto.objects.all()

    context = {
        'form' : form,
        'produtos' : produtos
    }

    return render(request, 'index.html', context)