from django.shortcuts import render
from django.contrib import messages
from .models import RegistroAtendimento

from .forms import RegistroAtendimentoForm

def usuarios_atendimento(reuqest):
    usuario_logado = reuqest.user

    return str(usuario_logado)

def registro_atendimento(request):
    if str(request.method) == 'POST':
        form = RegistroAtendimentoForm(request.POST)
        if form.is_valid():   
            form.save()
            messages.success(request, 'Empreendedor salvo com sucesso!')
            form = RegistroAtendimentoForm()
        else:
            messages.success(request, 'Erro ao salvar Empreendedor!')
    else:
        form = RegistroAtendimentoForm()
    context = {
            'form': form
    }
    return render(request, 'registro_atendimento.html', context)

def registros(request):
    context = {
        'registros': RegistroAtendimento.objects.all()
    }
    return render(request, 'registros.html', context)

