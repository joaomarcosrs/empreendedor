from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


def cadastro_user(request):
    return render(request, 'cadastro.html')

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print(username)
            if user:
                login(request, user)
                return HttpResponseRedirect('home')
            else:
                messages.success(request, 'Usuário e/ou Senha inválidos!')
            return render(request, "login.html")

def home(request):
    if request.user.is_authenticated:
        context = {
            'usuario_logado': request.user
        }
        return render (request, 'home.html', context)
    else:
        return redirect('login')