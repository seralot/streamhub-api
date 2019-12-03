from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField("Director", max_length=30, blank=False, null=False)
    surname = models.CharField(("Apellidos"), max_length=50)
    photo = models.CharField(("Foto"), max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "director"
        verbose_name_plural = "Directores"


class Platform(models.Model):
    name = models.CharField("Nombre", max_length=20, blank=False, null=False)
    pricePremium = models.IntegerField("Premium")
    priceStandard = models.IntegerField("Estandár")
    priceBasic = models.IntegerField("Basico")
    content4k = models.BooleanField("4K")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "plataforma"
        verbose_name_plural = "Plataformas"


class Content(models.Model):
    MOVIE = "Pelicula"
    SERIE = "Serie"
    DOCUMENTAL = "Documental"
    TYPE_CHOICES = [(MOVIE, "Pelicula"), (SERIE, "Serie"), (DOCUMENTAL, "Documental")]
    typeContent = models.CharField(
        "Tipo", max_length=12, choices=TYPE_CHOICES, default=MOVIE
    )
    title = models.CharField("Titulo", max_length=50, blank=False, null=False)
    release = models.DateField("Estreno", blank=False, null=False)
    runtime = models.IntegerField("Duración")
    genre = models.TextField("Genero", max_length=40)
    episodes = models.IntegerField("Capitulos", blank=True, null=True)
    seasons = models.IntegerField("Temporadas", blank=True, null=True)
    description = models.TextField("Descripción")
    poster = models.CharField("Poster", max_length=150)
    imdbRating = models.CharField("IMDB", max_length=6)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.release}"

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural = "Contenido"


class PlatformContent(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    num_seasons = models.IntegerField("Temporadas", blank=True, null=True)
    num_episodes = models.IntegerField("Capitulos", blank=True, null=True)

    def __str__(self):
        return f"{self.platform} {self.content}"

    class Meta:
        verbose_name = "Contenido Plataforma"
        verbose_name_plural = "Contenido Plataformas"
