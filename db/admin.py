from typing import Callable, Optional, TypeVar

from django.contrib import admin

from . import models

# Register your models here.

ReturnType = TypeVar("ReturnType")
FuncType = Callable[..., ReturnType]
Func = TypeVar("Func", bound=FuncType)

# Source https://github.com/escaped/django-admin-display
def admin_display(
    admin_order_field: Optional[str] = None,
    boolean: Optional[bool] = None,
    empty_value_display: Optional[str] = None,
    short_description: Optional[str] = None,
) -> Callable[[Func], Func]:
    def wrapper(func: Func) -> Func:
        if admin_order_field is not None:
            setattr(func, "admin_order_field", admin_order_field)
        if boolean is not None:
            setattr(func, "boolean", boolean)
        if empty_value_display is not None:
            setattr(func, "empty_value_display", empty_value_display)
        if short_description is not None:
            setattr(func, "short_description", short_description)
        return func

    return wrapper


@admin.register(models.Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "release",
        "runtime",
        "director",
        "genre",
        "imdbRating",
        "typeContent",
    )
    list_filter = ("typeContent",)


@admin.register(models.PlatformContent)
class PlatformContentAdmin(admin.ModelAdmin):
    list_display = (
        "platform",
        "title",
        "release",
        "runtime",
        "imdbRating",
        "typeContent",
    )
    list_filter = ("platform",)

    @admin_display(short_description="Titulo")
    def title(self, obj):
        return obj.content.title

    @admin_display(short_description="Estreno")
    def release(self, obj):
        return obj.content.release

    @admin_display(short_description="Duración")
    def runtime(self, obj):
        return obj.content.runtime

    @admin_display(short_description="Puntuación")
    def imdbRating(self, obj):
        return obj.content.imdbRating

    @admin_display(short_description="Tipo")
    def typeContent(self, obj):
        return obj.content.typeContent


@admin.register(models.Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ("name", "pricePremium", "priceStandard", "priceBasic", "content4k")


@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")
