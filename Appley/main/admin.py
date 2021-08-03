from django.contrib import admin
from main.models import Fruit

@admin.register(Fruit)
class Fruit(admin.ModelAdmin):
    list_display = ('fruitname', 'ftype')
    search_fields = ('fFruitname', 'ftype')