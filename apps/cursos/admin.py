from django.contrib import admin

# Register your models here.
from .models import Cursos,Galeria


admin.site.register(Cursos)

class filto_fotos(admin.ModelAdmin):

    list_display=("curso",)
    
    list_filter =("curso",) 

admin.site.register(Galeria, filto_fotos)