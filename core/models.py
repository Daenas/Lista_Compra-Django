from django.db import models

class Produto(models.Model):
    Nome = models.CharField("Nome", max_length=100)
    Quantidade = models.CharField("Quantidade", max_length=100)

    def __str__(self):
        return f'{self.Nome} ({self.Quantidade})'
