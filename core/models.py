from django.db import models

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=100)
    quantidade = models.CharField("Quantidade", max_length=100)

    def __str__(self):
        return f'{self.nome} ({self.quantidade})'