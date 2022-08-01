from django.contrib import admin
from .models import Noticias


class Busqueda_noticias(admin.ModelAdmin):
    list_display=("titulo",)
    search_fields=("titulo",)
    list_filter =("categoria",)
    
admin.site.register(Noticias,Busqueda_noticias)