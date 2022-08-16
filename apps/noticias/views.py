from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Noticias,Categorias
from apps.cursos.models import Cursos
from django.http import HttpResponse, HttpResponseRedirect
from UOCRAong.sesion import login

from django.urls import reverse

# Create your views here.

class addNoticias(CreateView):
    model= Noticias
    fields=['categoria','titulo','introduccion', 'texto', 'imagenes','activo' ]
    template_name = 'noticias/addNoticias.html'
    success_url= reverse_lazy ('index')


def MostrarNoticia(request):
    noticia = Noticias.objects.all()
    categoria = Categorias.objects.all() 
    cursos = Cursos.objects.all()
    contexto = login(request)
    contexto['noticia'] = noticia
    contexto['categoria']= categoria
    contexto['cursos'] = cursos
    
  
    return render (request, 'noticias/listaNoticiasGeneral.html', contexto)
    

def ListarNoticiaPorCategoria(request, categoria):
    categoria2 = Categorias.objects.filter(nombre=categoria)
    noticia = Noticias.objects.filter(categoria = categoria2[0].id)  
    categoria = Categorias.objects.all() 
    cursos = Cursos.objects.all()
    contexto = login(request)
    contexto['categoria'] = categoria
    contexto['noticia'] = noticia
    contexto['cursos'] = cursos
    return render(request,'noticias/listaNoticias.html', contexto)

def noticia (request, id):
    noticia = Noticias.objects.get(id=id)
    categoria = Categorias.objects.all()
    cursos = Cursos.objects.all()
    contexto = login(request)
    contexto['noticia'] = noticia
    contexto['categoria'] = categoria
    contexto['cursos']= cursos

    return render(request, 'noticias/noticias.html',contexto)

def delete(request , id):
    noticia =Noticias.objects.get(id=id)
    noticia.delete()
    cursos = Cursos.objects.all()
    return HttpResponseRedirect(reverse('index'))
