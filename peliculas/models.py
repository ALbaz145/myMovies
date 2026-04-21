from django.db import models

class Estudio(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

class Genero(models.Model):
    LISTADO_GENEROS = [
        ('ACT', 'Acción'),
        ('COM', 'Comedia'),
        ('DRM', 'Drama'),
        ('SCI', 'Ciencia Ficción'),
        ('HOR', 'Horror'),
        ('ROM', 'Romance'),
        ('ANI', 'Animación'),
        ('AVN', 'Aventura'),
        ('FAN', 'Fantasía'),
        ('MUS', 'Musical'),
        ('DEF', 'Default'),
    ]
    nombre = models.CharField(max_length=3, choices=LISTADO_GENEROS, default='DEF')

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    fecha_lanzamiento = models.DateField()
    pais_origen = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=1000)
    estudio = models.ForeignKey(Estudio, on_delete=models.PROTECT)
    duracion = models.CharField(max_length=255)
    generos = models.ManyToManyField(Genero)
    imagen = models.ImageField(upload_to='peliculas/', null=True, blank=True)
    gross = models.CharField(max_length=255)

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    reviews = models.ForeignKey('Review', on_delete=models.CASCADE, null=True, blank=True)

class Review(models.Model):
    pelicula = models.OneToOneField(Pelicula, on_delete=models.CASCADE, primary_key=True)
    texto = models.TextField(max_length=1000)

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    pais = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='peliculas/', null=True, blank=True)

class PeliculaPersona(models.Model):
    LISTADO_ROLES = [
        ('ACT', 'Actor'),
        ('DIR', 'Director'),
        ('PRO', 'Productor'),
        ('ESC', 'Escritor')
    ]
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50, choices=LISTADO_ROLES, default='ACT')



