from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula, Persona, PeliculaPersona, Resena
from .forms import ResenaForm

def base(request):
    return render(request, "base.html")

def home(request):
    todas_las_pelis = Pelicula.objects.all().order_by('-id')
    ultima_pelicula = todas_las_pelis.first()
    
    if todas_las_pelis.count() > 1:
        peliculas_recientes = todas_las_pelis[1:5]
    else:
        peliculas_recientes = todas_las_pelis

    ultimas_resenas = Resena.objects.all().order_by('-id')[:3]
    
    return render(request, "home.html", {
        "pelicula": ultima_pelicula,
        "peliculas": peliculas_recientes,
        "reseñas": ultimas_resenas 
    })

def peliculas(request):
    items = Pelicula.objects.all().order_by('-id')
    return render(request, "peliculas.html", {"peliculas": items})

def pelicula_detalle(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    participaciones = PeliculaPersona.objects.select_related("persona").filter(pelicula=pelicula)
    reseñas_peli = Resena.objects.filter(pelicula=pelicula).order_by('-id')

    
    if request.method == "POST":
        form = ResenaForm(request.POST)
        if form.is_valid():
            nueva_resena = form.save(commit=False)
            nueva_resena.pelicula = pelicula  # 
            nueva_resena.save()
            return redirect('pelicula_detalle', pelicula_id=pelicula.id)
    else:
        form = ResenaForm()

    context = {
        "pelicula": pelicula,
        "participaciones": participaciones,
        "reseñas": reseñas_peli,
        "form": form, 
    }
    return render(request, "pelicula_detalle.html", context)

def persona_detalle(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    participaciones = PeliculaPersona.objects.select_related("pelicula").filter(persona=persona)
    return render(request, "persona_detalle.html", {"persona": persona, "participaciones": participaciones})