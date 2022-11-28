from django.shortcuts import render

def cadastro_user(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')
