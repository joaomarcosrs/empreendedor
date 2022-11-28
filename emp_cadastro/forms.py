from django import forms
from .models import RegistroAtendimento

class RegistroAtendimentoForm(forms.ModelForm):
    class Meta:
        model = RegistroAtendimento
        fields = [
            'nome',
            'cnpj', 
            'cpf', 
            'nascimento',
            'email', 
            'telefone_principal',
            'telefone_alternativo',
            'descricao',
        ]
        widgets = {'descricao': forms.CheckboxSelectMultiple(),}
        

        



