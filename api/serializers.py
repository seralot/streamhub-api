from django.contrib.auth.models import User, Group
from rest_framework import serializers

from db import models


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Director
        fields = ["name", "surname", "photo"]

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Actor
        fields = ["name", "surname", "photo"]
    
class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Genre
        fields = ["name"]

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Platform
        fields = ["name", "pricePremium", "priceStandard", "priceBasic", "content4k"]


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Content
        fields = [
            "typeContent",
            "title",
            "release",
            "runtime",
            "genre",
            "episodes",
            "seasons",
            "description",
            "poster",
            "imdbRating",
            "director",
        ]


class PlatformContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PlatformContent
        fields = ["platform", "content", "num_seasons"]

class ActorContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ActorContent
        fields = ["actor", "content", "main"]