from django.db import models
from django_cpf_cnpj.fields import CPFField, CNPJField
from multiselectfield import MultiSelectField


ABERTURA = 'ABERTURA MEI'
ALTERACAO = 'ALTERAÇÃO CADASTRAL'
INFO = 'INFORMAÇÕES'
DAS = 'EMISSÃO DAS'
PARC = 'PARCELAMENTO'
EMISSAO_PARC = 'EMISSÃO DE PARCELA'
CODIGO = 'CÓDIGO DE ACESSO'
REGULARIZE = 'REGULARIZE'
BAIXA = 'BAIXA MEI'
CANCELADO = 'REGISTRO BAIXADO'

descricao_atendimento = (
    (ABERTURA, 'FORMALIZAÇÃO'),
    (ALTERACAO, 'ALTERAÇÃO CADASTRAL'),
    (INFO, 'INFORMAÇÕES'),
    (DAS, 'EMISSÃO DAS'),
    (PARC, 'PARCELAMENTO'),
    (EMISSAO_PARC, 'EMISSÃO DE PARCELA'),
    (CODIGO, 'CÓDIGO DE ACESSO'),
    (REGULARIZE, 'REGULARIZE'),
    (BAIXA, 'BAIXA MEI'),
    (CANCELADO, 'REGISTRO BAIXADO'),
)

class RegistroAtendimento(models.Model):

    nome = models.CharField(max_length=120)
    cnpj = CNPJField()
    cpf = CPFField()
    nascimento = models.DateField()
    email = models.EmailField(max_length=100)
    telefone_principal = models.CharField(max_length=11)
    telefone_alternativo = models.CharField(max_length=11, blank=True)
    descricao = MultiSelectField(choices=descricao_atendimento, max_length=100, max_choices=4)
   
    def __str__(self):
        return self.nome
    
    def __unicode__(self):
        return self.__str__()
