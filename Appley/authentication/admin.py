from django.contrib import admin
from authentication.models import User

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')