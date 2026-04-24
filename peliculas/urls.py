from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("peliculas/", views.peliculas, name="peliculas"),
    path("peliculas/<int:pelicula_id>/", views.pelicula_detalle, name="pelicula_detalle"),
    path("personas/<int:persona_id>/", views.persona_detalle, name="persona_detalle"),
    path('accounts/signup/', views.signup, name='signup'),
]

