from django.contrib import admin
from .models import PT, Cliente, SessaoTreino

@admin.register(PT)
class PTAdmin(admin.ModelAdmin):
    list_display = ("nome", "especialidade")
    search_fields = ("nome", "especialidade")
    ordering = ("nome",)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade", "email")
    search_fields = ("nome", "email")
    ordering = ("nome",)


@admin.register(SessaoTreino)
class SessaoTreinoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "pt", "data", "hora")
    search_fields = ("cliente__nome", "pt__nome")
    ordering = ("data", "hora")