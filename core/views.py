from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def register(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        sobrenome = request.POST.get('surname')
        telefone = request.POST.get('number')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha2 = request.POST.get('passwordConfirm')
        
        # Validação simples da senha
        if senha != senha2:
            messages.error(request, "As senhas não coincidem.")
            return redirect('register')
        
        
        
        pass
    return render(request, "core/register.html")

def login(request):
    return render(request, "core/login.html")