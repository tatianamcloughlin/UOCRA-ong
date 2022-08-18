from django.shortcuts import render
from apps.noticias.models import Noticias,Categorias
from apps.cursos.models import Cursos
from UOCRAong.sesion import login
def inicio(request):
    noticia = Noticias.objects.all()[:3]
    categoria = Categorias.objects.all()
    cursos = Cursos.objects.all()
    contexto = login(request)
    contexto['noticia'] = noticia
    contexto['categoria'] = categoria
    contexto['cursos'] = cursos
    

    return render(request, 'inicio.html',contexto)


def index (request):
    return render(request, 'index.html')

def registro (request):
    return render(request, 'registro.html')