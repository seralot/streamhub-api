from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Movie)
admin.site.register(models.Director)
admin.site.register(models.Platform)
admin.site.register(models.PlatformContent)