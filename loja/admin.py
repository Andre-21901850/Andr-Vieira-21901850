from django.contrib import admin
from .models import Categoria, Produto, Cliente, Morada, Pedido, ItemPedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "stock", "categoria")
    search_fields = ("nome",)
    ordering = ("nome",)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome", "email")
    ordering = ("nome",)


@admin.register(Morada)
class MoradaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "rua", "cidade", "codigo_postal")
    search_fields = ("cliente__nome", "cidade")
    ordering = ("cidade",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "data")
    search_fields = ("cliente__nome",)
    ordering = ("-data",)


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "produto", "quantidade")
    search_fields = ("produto__nome",)
    ordering = ("pedido",)