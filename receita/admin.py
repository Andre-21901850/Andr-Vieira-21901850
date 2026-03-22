from django.contrib import admin
from .models import Ingrediente, Receita

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)
    filter_horizontal = ("ingredientes", "favoritas")