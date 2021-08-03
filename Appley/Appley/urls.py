from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("main.urls")),

]
