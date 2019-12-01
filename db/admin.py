from django.contrib import admin

from . import models
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release', 'runtime', 'director', 'imdbRating', 'platform')
    list_filter = ('platform',)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'release', 'runtime', 'director', 'imdbRating', 'typeContent', 'platform')
    list_filter = ('platform',)

class ContentInline(admin.TabularInline):
    model = models.Content
    readonly_fields = ('title', 'release', 'runtime', 'director','imdbRating','typeContent')
    exclude = ('episodes','seasons', 'description','poster')
   
class ContentPlatform(admin.ModelAdmin):
    fieldsets = [
        ('Plataforma',               {'fields': ['name', 'price']})
    ]
    inlines = [ContentInline]


admin.site.register(models.Content, ContentAdmin)
admin.site.register(models.Director)
admin.site.register(models.Platform, ContentPlatform)

