from django.shortcuts import render
from apps.noticias.models import Noticias,Categorias
from apps.cursos.models import Cursos

def inicio(request):
    noticia = Noticias.objects.all()[:3]
    categoria = Categorias.objects.all()
    cursos = Cursos.objects.all()

    return render(request, 'inicio.html',{'noticia':noticia,'categoria':categoria, 'cursos':cursos })


def index (request):
    return render(request, 'index.html')