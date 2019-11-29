from django.contrib import admin

from . import models
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release', 'runtime', 'director', 'imdbRating', 'platform')
    list_filter = ('platform',)

class SerieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release', 'runtime', 'episodes', 'seasons', 'director', 'imdbRating', 'platform')
    list_filter = ('platform',)

admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Serie, SerieAdmin)

admin.site.register(models.Director)
admin.site.register(models.Platform)


