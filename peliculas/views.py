from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Pelicula, Persona

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

def persona_detalle(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)

    participaciones = (
        PeliculaPersona.objects
        .select_related("pelicula")
        .filter(persona=persona)
        .order_by("pelicula__titulo")
    )

    return render(request, "persona_detalle.html", {
        "persona": persona,
        "participaciones": participaciones,
    })

