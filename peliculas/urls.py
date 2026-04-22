from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("peliculas/", views.peliculas, name="peliculas"),
    path("peliculas/<int:pelicula_id>/", views.pelicula_detalle, name="pelicula_detalle"),
]