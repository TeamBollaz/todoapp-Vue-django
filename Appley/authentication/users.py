from rest_framework import serializers
from django.conf.urls import include, url
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=(
            "url",
            "id",
            "username",
            "email",
            "is_staff"
        )