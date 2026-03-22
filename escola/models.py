from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    ano_escolar = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.ano_escolar}"


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    turma = models.OneToOneField(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="alunos")

    def __str__(self):
        return self.nome