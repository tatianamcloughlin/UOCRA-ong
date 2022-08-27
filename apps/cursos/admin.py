from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Cursos,Galeria


admin.site.register(Cursos)

class filto_fotos(admin.ModelAdmin):

    list_display=("curso","imagen", "foto")
    
    list_filter =("curso","fecha",) 

    def foto(self,obj):
        return format_html('<img src={} width=100>', obj.imagen.url)

admin.site.register(Galeria, filto_fotos)