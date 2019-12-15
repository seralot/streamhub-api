from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField("Nombre", max_length=30, blank=False, null=False)
    surname = models.CharField(("Apellidos"), max_length=50)
    photo = models.CharField(("Foto"), max_length=150)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "director"
        verbose_name_plural = "Directores"

class Actor(models.Model):
    name = models.CharField("Nombre", max_length=30, blank=False, null=False)
    surname = models.CharField(("Apellidos"), max_length=50)
    photo = models.CharField(("Foto"), max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "actor"
        verbose_name_plural = "Actores"

class Genre(models.Model):
    name = models.CharField("Genero", max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "genero"
        verbose_name_plural = "Generos"

class Platform(models.Model):
    name = models.CharField("Nombre", max_length=20, blank=False, null=False)
    urlLogo = models.CharField("Logo", max_length=150)
    pricePremium = models.DecimalField("Precio Premium", max_digits=5, decimal_places=2)
    priceStandard = models.DecimalField("Precio Estandár", max_digits=5, decimal_places=2)
    priceBasic = models.DecimalField("Precio Basico", max_digits=5, decimal_places=2)
    resolutionPremium = models.CharField("Resolución Premium", max_length=10)
    resolutionStandard = models.CharField("Resolución Estandár", max_length=10)
    resolutionBasic = models.CharField("Resolución Basico", max_length=10)
    devicesPremium = models.IntegerField("Dispositivos Premium")
    devicesStandard = models.IntegerField("Dispositivos Estandár")
    devicesBasic = models.IntegerField("Dispositivos Basico")
    profiles = models.IntegerField("Perfiles")
    parentalControl = models.BooleanField("Control Parental")
    noConnection = models.BooleanField("Sin Conexión")

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
    episodes = models.IntegerField("Capitulos", blank=True, null=True)
    seasons = models.IntegerField("Temporadas", blank=True, null=True)
    description = models.TextField("Descripción")
    poster = models.CharField("Poster", max_length=150)
    trailer = models.CharField("Trailer", max_length=150)
    imdbRating = models.CharField("IMDB", max_length=6)
    sorting = models.CharField("Clasificación", max_length=6)
    director = models.ManyToManyField(Director)
    genre = models.ManyToManyField(Genre, verbose_name='Genero',)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural = "Contenido"


class PlatformContent(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    num_seasons = models.IntegerField("Temporadas", blank=True, null=True)
    url = models.CharField("Enlace", max_length=150)

    def __str__(self):
        return f"{self.platform} {self.content}"

    class Meta:
        verbose_name = "Contenido Plataforma"
        verbose_name_plural = "Contenido Plataformas"

class ActorContent(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    main = models.BooleanField("Principal")

    def __str__(self):
        return f"{self.actor} {self.content}"

    class Meta:
        verbose_name = "actor contenido"
        verbose_name_plural = "Actores Contenido"