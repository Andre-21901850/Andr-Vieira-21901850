from django.contrib import admin
from .models import Artigo, Comentario

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('autor', 'data_criacao')
    search_fields = ('texto', 'autor__username')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'artigo', 'data')
    search_fields = ('texto', 'autor__username')