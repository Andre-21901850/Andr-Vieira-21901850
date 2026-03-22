from django.db import models

class PT(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class SessaoTreino(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="sessoes")
    pt = models.ForeignKey(PT, on_delete=models.CASCADE, related_name="sessoes")
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.cliente} com {self.pt} em {self.data} às {self.hora}"

    class Meta:
        unique_together = ('pt', 'data', 'hora')