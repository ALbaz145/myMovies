from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Pelicula, Persona, PeliculaPersona

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

    participaciones = (
        PeliculaPersona.objects
        .select_related("persona")
        .filter(pelicula=pelicula)
        .order_by("rol", "persona__nombre")
    )

    context = {
        "pelicula": pelicula,
        "participaciones": participaciones,
    }
    return render(request, "pelicula_detalle.html", context)

def persona_detalle(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)

    participaciones = (
        PeliculaPersona.objects
        .select_related("pelicula")
        .filter(persona=persona)
        .order_by("rol", "pelicula__titulo")
    )

    context = {
        "persona": persona,
        "participaciones": participaciones,
    }
    return render(request, "persona_detalle.html", context)



