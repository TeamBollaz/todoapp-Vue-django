from django.shortcuts import render,HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from authentication import models
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import routers, viewsets, serializers
from .users import UserSerializer

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "auth/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
  

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "auth/register.html", {"form": form, "msg" : msg, "success" : success })

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserViewset(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewset) 