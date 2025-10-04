from django.db import models
from django.contrib.auth.models import User

class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.bairro}"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
