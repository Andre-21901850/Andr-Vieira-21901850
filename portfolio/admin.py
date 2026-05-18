from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular, Tecnologia, Projeto, TFC

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'ano_inicio', 'ano_fim')
    search_fields = ('nome', 'instituicao')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'ano', 'semestre', 'ects', 'licenciatura')
    search_fields = ('nome', 'codigo')
    list_filter = ('ano', 'semestre', 'licenciatura')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel_interesse')
    search_fields = ('nome', 'categoria')
    list_filter = ('nivel_interesse', 'categoria')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uc', 'data')
    search_fields = ('nome', 'descricao')
    list_filter = ('uc', 'tecnologias')

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano', 'nivel_interesse')
    search_fields = ('titulo', 'autor')
    list_filter = ('ano', 'nivel_interesse')