from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular

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