from django.contrib import admin
from .models import Pessoa, Endereco


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'usuario', 'cargo')
	search_fields = ('nome', 'cpf', 'email', 'usuario__username')


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
	list_display = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'cep')
