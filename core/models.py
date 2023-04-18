from django.db import models
from django.db.models import signals

class Produto(models.Model):
    Nome = models.CharField("Nome", max_length=100)
    Quantidade = models.CharField("Quantidade", max_length=100)

    def __str__(self):
        return f'{self.Nome} ({self.Quantidade})'
    

"""
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.Nome = instance.Nome.title


signals.pre_save.connect(produto_pre_save, sender=Produto)
"""