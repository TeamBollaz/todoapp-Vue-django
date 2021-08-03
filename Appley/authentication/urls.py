from django.urls import path
from django.conf.urls import include, url
from .views import login_view, register_user, UserSerializer 
from django.contrib.auth.views import LogoutView
from authentication import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("api/", include(views.router.urls)),
    path("authuser/", include('rest_framework.urls', namespace='rest_framework')),
   
]