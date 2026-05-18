from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    ano_inicio = models.IntegerField()
    ano_fim = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    link_pagina = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, blank=True)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    docentes = models.ManyToManyField(Docente, related_name='ucs', blank=True)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    NIVEL_CHOICES = [
        (1, 'Iniciante'),
        (2, 'Básico'),
        (3, 'Intermédio'),
        (4, 'Avançado'),
        (5, 'Especialista'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    link_website = models.URLField(blank=True)
    nivel_interesse = models.IntegerField(choices=NIVEL_CHOICES, default=3)
    categoria = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome