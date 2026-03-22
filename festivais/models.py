from django.db import models

class GeneroMusical(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE, related_name="bandas")

    def __str__(self):
        return self.nome


class Festival(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    data = models.DateField()
    bandas = models.ManyToManyField(Banda, related_name="festivais")

    def __str__(self):
        return self.nome