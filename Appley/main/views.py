from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from authentication import models
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Fruit
from .fruits import FruitSerializer
from rest_framework import routers, viewsets, serializers

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'home.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-page.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-page.html' )
        return HttpResponse(html_template.render(context, request))

class FruitList(APIView):
    def get(self, request, format=None):
        fruits = Fruit.objects.all()
        serializer = FruitSerializer(fruits, many=True)
        return Response(serializer.data)


class FruitViewset(viewsets.ModelViewSet):
        queryset = Fruit.objects.all()
        serializer_class = FruitSerializer

router = routers.DefaultRouter()
router.register(r'fruits', FruitViewset)

