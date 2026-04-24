from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula, Persona, PeliculaPersona, Resena
from .forms import ResenaForm
from django.db.models import Avg, Value
from django.db.models.functions import Coalesce

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

    
    ids_excluir = []
    if ultima_pelicula:
        ids_excluir.append(ultima_pelicula.id)
    ids_excluir += [p.id for p in peliculas_recientes]

    
    candidatas = (
        Pelicula.objects
        .exclude(id__in=ids_excluir)
        .annotate(prom_calificacion=Coalesce(Avg('resenas__calificacion'), Value(0.0)))
        .order_by('-prom_calificacion', '-id')
    )


    if candidatas.count() < 3:
        candidatas = (
            Pelicula.objects
            .exclude(id=ultima_pelicula.id) if ultima_pelicula else Pelicula.objects.all()
        ).annotate(
            prom_calificacion=Coalesce(Avg('resenas__calificacion'), Value(0.0))
        ).order_by('-prom_calificacion', '-id')

    recomendadas = list(candidatas[:6])

    return render(request, "home.html", {
        "pelicula": ultima_pelicula,
        "peliculas": peliculas_recientes,
        "reseñas": ultimas_resenas,
        "recomendadas": recomendadas,
    })

def peliculas(request):
    query = request.GET.get('q', '') # Captura lo que escribes en la lupa
    if query:
        items = Pelicula.objects.filter(
            Q(titulo__icontains=query) | 
            Q(sinopsis__icontains=query)
        ).distinct().order_by('-id')
    else:
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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})