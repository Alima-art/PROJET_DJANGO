from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'home.html')


def connexion(request):
    return render(request, 'connexion.html')


def register(request):
    return render(request, 'register.html')


def inscrire(request):
    return render(request, 'inscrire.html')


def nous(request):
    return render(request, 'nous.html')


def detail(request, IDu):
    return render("You're looking at question %s." % IDu)
