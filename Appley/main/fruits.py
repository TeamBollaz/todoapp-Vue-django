from rest_framework import serializers
from django.conf.urls import include, url
from .models import Fruit

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields=(
            'url',
            "id",
            "fruitname",
            "ftype",
            "region"
        )