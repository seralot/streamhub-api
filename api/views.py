from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from db import models
from api import serializers

# Create your views here.


class DirectorViewSet(viewsets.ModelViewSet):

    queryset = models.Director.objects.all().order_by("name")
    serializer_class = serializers.DirectorSerializer

class ActorViewSet(viewsets.ModelViewSet):

    queryset = models.Actor.objects.all().order_by("name")
    serializer_class = serializers.ActorSerializer

class GenreViewSet(viewsets.ModelViewSet):

    queryset = models.Genre.objects.all().order_by("name")
    serializer_class = serializers.GenreSerializer

class PlatformViewSet(viewsets.ModelViewSet):

    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer


class ContentViewSet(viewsets.ModelViewSet):

    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer


class PlatformContentViewSet(viewsets.ModelViewSet):

    queryset = models.PlatformContent.objects.all()
    serializer_class = serializers.PlatformContentSerializer

class ActorContentViewSet(viewsets.ModelViewSet):

    queryset = models.ActorContent.objects.all()
    serializer_class = serializers.ActorContentSerializer