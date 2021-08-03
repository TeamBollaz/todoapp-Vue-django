from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from .models import Fruit
from django.urls import path, include
from rest_framework import routers, viewsets, serializers
from main import views
   

urlpatterns = [
    path('', views.index, name = 'home'),
    path("apifruit/", include(views.router.urls)),
    path("fruit/", include('rest_framework.urls', namespace='rest')),
]
