from django.shortcuts import render
from apps.noticias.models import Noticia, Categoria
from apps.curso.models import Categoria_curso
from django.contrib.auth.hashers import check_password
from UOCRAong.sesion import login

def index(request):
    noticia = Noticia.objects.raw("SELECT * FROM noticias_noticia ORDER BY fecha")[:3]
    categoria = Categoria.objects.all()      

    contexto = login(request)         
    contexto['noticia'] = noticia
    contexto['categoria'] = categoria
    
    return render(request, 'index.html',contexto)




def noticias(request):
    contexto = login(request)
    noticia = Noticia.objects.raw("SELECT * FROM noticias_noticia WHERE id={}".format(request.GET['id']))
    categoria = Categoria.objects.all()      
    categoria_curso = Categoria_curso.objects.all()
    contexto['noticia'] = noticia
    contexto['categoria_curso'] = categoria_curso
    contexto['categoria'] = categoria
    return render(request, 'noticias.html',contexto)