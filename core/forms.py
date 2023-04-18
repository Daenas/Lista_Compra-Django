from django import forms

from .models import Produto

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['Nome', 'Quantidade']


"""
class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", min_length=1)
    quantidade = forms.CharField(label="Quantidade")
"""