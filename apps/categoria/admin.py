from django.contrib import admin
from .models import Categorias
# Register your models here.

class Categorias_atributos(admin.ModelAdmin):
    list_display =("categoria",)

admin.site.register(Categorias,Categorias_atributos)