from django.contrib import admin
from .models import Categoria, Noticia


class Busqueda_noticias(admin.ModelAdmin):
    search_fields=("titulo",)
    list_filter =("categoria",)
    
admin.site.register(Noticia,Busqueda_noticias)
admin.site.register(Categoria)