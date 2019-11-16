from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField("Title", max_length=50, blank=False, null=False)
    release = models.DateField("Release", blank=False, null=False)
    runtime = models.IntegerField("Time")
    director = models.CharField("Director", max_length=30)
    description = models.TextField("Description")
    poster = models.CharField("Poster", max_length=150)
    imdbRating = models.CharField("IMDB", max_length=6)
    platform = models.CharField("Streaming", max_length=100)

    def __str__(self):
        return f"{self.title} {self.release}"