from django.shortcuts import render


def index(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def register(request):
    return render(request, "core/register.html")

def login(request):
    return render(request, "core/login.html")