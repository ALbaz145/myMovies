from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Pelicula

# Create your views here.
def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")

def peliculas(request):
    items = Pelicula.objects.all()
    return render(request, "peliculas.html", {"peliculas": items })

def pelicula_detalle(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    return render(request, "pelicula_detalle.html", {"pelicula": pelicula})