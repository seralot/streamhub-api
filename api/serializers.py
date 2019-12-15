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
        fields = [
            "name",
            "urlLogo", 
            "pricePremium", 
            "priceStandard", 
            "priceBasic",
            "resolutionPremium",
            "resolutionStandard",
            "resolutionBasic",
            "devicesPremium",
            "devicesStandard",
            "devicesBasic",
            "profiles",
            "parentalControl",
            "noConnection"]


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    director = DirectorSerializer(many=True, read_only=True)
    
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
            "trailer",
            "director",
        ]


class PlatformContentSerializer(serializers.HyperlinkedModelSerializer):
    platform = serializers.StringRelatedField()
    content = ContentSerializer("title")
    class Meta:
        model = models.PlatformContent
        fields = ["platform", "content", "url", "num_seasons"]

class ActorContentSerializer(serializers.HyperlinkedModelSerializer):
    actor = ActorSerializer()
    content = serializers.StringRelatedField()
    class Meta:
        model = models.ActorContent
        fields = ["content", "actor", "main"]