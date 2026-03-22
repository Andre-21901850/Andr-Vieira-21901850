from django.contrib import admin
from .models import GeneroMusical, Banda, Festival

@admin.register(GeneroMusical)
class GeneroMusicalAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)


@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    list_display = ("nome", "genero")
    search_fields = ("nome", "genero__nome")
    ordering = ("nome",)


@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome", "local", "data")
    search_fields = ("nome", "local")
    ordering = ("nome",)
    filter_horizontal = ("bandas",)