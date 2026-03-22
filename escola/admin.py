from django.contrib import admin
from .models import Turma, Professor, Aluno

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano_escolar")
    search_fields = ("nome",)
    ordering = ("nome",)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "turma")
    search_fields = ("nome", "email")
    ordering = ("nome",)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade", "turma")
    search_fields = ("nome",)
    ordering = ("nome",)