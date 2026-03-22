from django.db import models
from django.contrib.auth.models import User

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente, related_name="receitas")
    favoritas = models.ManyToManyField(User, blank=True, related_name="receitas_favoritas")

    def __str__(self):
        return self.nome