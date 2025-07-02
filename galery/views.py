from django.shortcuts import render


def galery(request):
    return render(request, "galery/galeria.html")
