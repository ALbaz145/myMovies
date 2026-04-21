from django.shortcuts import render, HttpResponse
from .models import Pelicula

# Create your views here.
def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")

def peliculas(request):
    items = Pelicula.objects.all()
    return render(request, "peliculas.html", {"peliculas": items })