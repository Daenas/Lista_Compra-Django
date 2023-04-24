from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoModelForm
from django.contrib import messages
from django.views.generic import TemplateView


class IndexView(TemplateView):

    def get(self, request):
        form = ProdutoModelForm()
        produtos = Produto.objects.all()
        context = {
            'form': form,
            'produtos': produtos
        }
        return render(request, 'index.html', context)

    def post(self, request):

        form = ProdutoModelForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Produto salvo com sucesso!")
            form = ProdutoModelForm()

        else:
            messages.error(request, "Erro ao cadastrar produto.")

        form = ProdutoModelForm()
        produtos = Produto.objects.all()
        context = {
            'form': form,
            'produtos': produtos
        }

        return render(request, 'index.html', context)

def delete_event(request, event_id):
    event = Produto.objects.get(pk=event_id)
    event.delete()
    return redirect('index')