from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
