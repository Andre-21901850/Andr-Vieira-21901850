from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="produtos")

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Morada(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name="morada")
    rua = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.rua}, {self.cidade}"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.produto.nome} x {self.quantidade}"