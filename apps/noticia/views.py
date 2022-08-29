from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Noticia,Categoria,Comentario
from apps.curso.models import Curso
from django.http import HttpResponse, HttpResponseRedirect
from UOCRAong.sesion import login
from django.db import connection
from django.urls import reverse
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.




def MostrarNoticia(request):
    noticia = Noticia.objects.all()
    categoria = Categoria.objects.all() 
    cursos = Curso.objects.all()
    contexto = login(request)
    contexto['noticia'] = noticia
    contexto['categoria']= categoria
    contexto['cursos'] = cursos
    
  
    return render (request, 'noticia/listaNoticiasGeneral.html', contexto)
    

def ListarNoticiaPorCategoria(request, categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia = Noticia.objects.filter(categoria = categoria2[0].id)  
    categoria = Categoria.objects.all() 
    cursos = Curso.objects.all()

    paginator = Paginator (noticia, 6)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    
    index = items.number -1
    max_index = len(paginator.page_range)
    start_index = index-3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index -3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    contexto = login(request)
    contexto['categoria'] = categoria
    contexto['noticia'] = noticia
    contexto['cursos'] = cursos
    contexto['page_range'] = page_range
    contexto['items']= items


    return render(request,'noticia/listaNoticias.html', contexto)






def noticia (request, id):
    noticia = Noticia.objects.get(id=id)
    categoria = Categoria.objects.all()
    cursos = Curso.objects.all()
    comentario = Comentario.objects.filter(noticia_id=id,).order_by('-fecha')
    contexto = login(request)
    contexto['noticia'] = noticia
    contexto['categoria'] = categoria
    contexto['cursos']= cursos
    contexto['comentarios']= comentario
    try:

        print(request.POST.get('contenido'))
        print(request.POST.get('id'))
        print(request.POST.get('idusuario'))
        with connection.cursor() as cursor:
               cursor.execute(f"INSERT INTO noticia_comentario (comentario,fecha,noticia_id,usuario_id) VALUES ('{request.POST.get('contenido')}','{datetime.now()}',{request.POST.get('id')},'{request.POST.get('idusuario')}')")
                
    except Exception as e:
        print(e)

        return render(request, 'noticia/noticia.html',contexto)

    else:
        return HttpResponseRedirect('/noticia/noticia/{}'.format(id))
    




