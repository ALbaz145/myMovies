from django.contrib import admin
from .models import Pelicula, Estudio, Genero, Resena, Persona, PeliculaPersona

admin.site.register(Estudio)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Resena)
admin.site.register(Persona)
admin.site.register(PeliculaPersona)
