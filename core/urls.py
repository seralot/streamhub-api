"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'director', views.DirectorViewSet)
router.register(r'actor', views.ActorViewSet)
router.register(r'genre', views.GenreViewSet)
router.register(r'platform', views.PlatformViewSet)
router.register(r'content', views.ContentViewSet)
router.register(r'platformContent', views.PlatformContentViewSet)
router.register(r'actorContent', views.ActorContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]

# Styles Django Admin
admin.site.site_header = "Streamhub Admin"
admin.site.site_title = "Streamhub Admin Portal"
admin.site.index_title = "Streamhub Admin"