from django.contrib import admin
from .models import Noticias,Categorias,Comentario


class Busqueda_noticias(admin.ModelAdmin):
    list_display=("titulo",)
    search_fields=("titulo",)
    list_filter =("categoria",)
    
admin.site.register(Noticias,Busqueda_noticias)

class Categorias_atributos(admin.ModelAdmin):
    list_display =("nombre",)

class Filtros(admin.ModelAdmin):
    list_filter =("fecha",'usuario')
admin.site.register(Categorias,Categorias_atributos, )
admin.site.register(Comentario,Filtros)