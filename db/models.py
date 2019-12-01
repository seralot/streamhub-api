from django.db import models

# Create your models here.

    
class Director(models.Model):
    name = models.CharField('Director', max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "director" 
        verbose_name_plural = "Directores"

class Platform(models.Model):
    name = models.CharField('Nombre', max_length=20, blank=False, null=False)
    price = models.IntegerField("Precio")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "plataforma"  
        verbose_name_plural = "Plataformas"

# class Movie(models.Model):
#     title = models.CharField("Titulo", max_length=50, blank=False, null=False)
#     release = models.DateField("Estreno", blank=False, null=False)
#     runtime = models.IntegerField("Duración")
#     description = models.TextField("Descripción")
#     poster = models.CharField("Poster", max_length=150)
#     imdbRating = models.CharField("IMDB", max_length=6)
#     director = models.ForeignKey(Director, on_delete=models.CASCADE)
#     platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.title} {self.release}"
    
#     class Meta: 
#         verbose_name = "pelicula"  
#         verbose_name_plural = "Peliculas"

class Content(models.Model):
    title = models.CharField("Titulo", max_length=50, blank=False, null=False)
    release = models.DateField("Estreno", blank=False, null=False)
    runtime = models.IntegerField("Duración")
    episodes = models.IntegerField("Capitulos")
    seasons = models.IntegerField("Temporadas")
    description = models.TextField("Descripción")
    poster = models.CharField("Poster", max_length=150)
    imdbRating = models.CharField("IMDB", max_length=6)
    typeContent = models.CharField("Tipo", max_length=10, blank=False, default="Pelicula")
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.release}"
    
    class Meta: 
        verbose_name = "Contenido"
        verbose_name_plural = "Contenido"




# class Serie(models.Model):
#     title = models.CharField("Titulo", max_length=50, blank=False, null=False)
#     release = models.DateField("Estreno", blank=False, null=False)
#     runtime = models.IntegerField("Duración Episodio")
#     episodes = models.IntegerField("Capitulos")
#     seasons = models.IntegerField("Temporadas")
#     description = models.TextField("Descripción")
#     poster = models.CharField("Poster", max_length=150)
#     imdbRating = models.CharField("IMDB", max_length=6)
#     director = models.ForeignKey(Director, on_delete=models.CASCADE)
#     platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.title} {self.release}"
    
#     class Meta: 
#         verbose_name_plural = "Series"


