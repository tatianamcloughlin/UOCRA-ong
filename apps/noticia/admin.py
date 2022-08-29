from django.contrib import admin
from .models import Noticia,Categoria,Comentario


class Busqueda_noticias(admin.ModelAdmin):
    list_display=("titulo",)
    search_fields=("titulo",)
    list_filter =("categoria",)
    
admin.site.register(Noticia,Busqueda_noticias)

class Categoria_atributos(admin.ModelAdmin):
    list_display =("nombre",)

class Filtros(admin.ModelAdmin):
    list_filter =("fecha",'usuario')
admin.site.register(Categoria,Categoria_atributos, )
admin.site.register(Comentario,Filtros)