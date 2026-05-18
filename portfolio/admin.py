from django.contrib import admin
from .models import Licenciatura, Docente

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'ano_inicio', 'ano_fim')
    search_fields = ('nome', 'instituicao')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')