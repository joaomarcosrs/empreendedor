from django.contrib import admin
from .models import RegistroAtendimento

admin.site.register(RegistroAtendimento)

class RegistroAtendimentoAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'cpf', 'nome', 'nascimento', 'email', 'telefone_principal', 'telefone_alternativo', 'descricao', 'tipo', 'criado')
