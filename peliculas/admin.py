from django.contrib import admin
from .models import Pelicula, Estudio, Genero
# Register your models here.
admin.site.register(Estudio)
admin.site.register(Genero)
admin.site.register(Pelicula)
