from multiprocessing import context
from sqlite3 import Cursor
from django.shortcuts import render
from apps.curso.models import Curso , Galeria
from apps.noticia.models import Categoria
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from UOCRAong.sesion import login
from apps.usuario.models import UsuarioManager

from django.db import connection


def curso (request, nombre ):
    curso2= Curso.objects.get(nombre=nombre)
    categoria= Categoria.objects.all()
    cursos = Curso.objects.all()
    contexto = login(request)
    contexto['curso'] = curso2
    contexto['categoria'] = categoria
    contexto['cursos'] = cursos
    return render(request, 'cursos/basecursos.html', contexto)



class addFotos(CreateView):
    model= Galeria
    fields=['curso','imagen','activo' ]
    template_name = 'cursos/addFotos.html'
    success_url= reverse_lazy ('apps.curso:galeria')



def ListaFotosPorCurso(request, nombre):
    curso= Curso.objects.get(nombre=nombre)
    curso1 = Curso.objects.filter (nombre=nombre)
    foto = Galeria.objects.filter(curso = curso1[0].id)  
    cursos = Curso.objects.all()
    categoria= Categoria.objects.all()
    contexto = login(request)
    contexto['foto'] = foto
    contexto['cursos']= cursos
    contexto['categoria'] = categoria
    contexto['curso'] = curso

    try:
        id_foto= request.POST.get('idFoto')
        borrar = Galeria.objects.get(id=id_foto)
        borrar.delete()
    except Exception as e:
        print(e)

    return render(request,'cursos/galeria.html', contexto)



def MostrarGaleria(request):
    foto = Galeria.objects.all()    
    curso = Curso.objects.all()
    categoria= Categoria.objects.all()
    

    
    contexto = login(request)
    contexto['foto'] = foto
    contexto['cursos'] = curso
    contexto['categoria'] = categoria
    
    try:
        id_foto= request.POST.get('idFoto')
        borrar = Galeria.objects.get(id=id_foto)
        borrar.delete()
    except Exception as e:
        print(e)
  
    return render (request, 'cursos/galeriaGeneral.html', contexto)





# Create your views here.
def EliminarFoto (request): 
    foto = Galeria.objects.all()    
    curso = Curso.objects.all()
    categoria= Categoria.objects.all()
    
    contexto = login(request)
    contexto['foto'] = foto
    contexto['cursos'] = curso
    contexto['categoria'] = categoria
    
    try:
        print(request.POST.get('id.foto'))
        with connection.cursor() as cursor:
               cursor.execute (f"DELETE FROM 'curso_galeria' WHERE id='{request.POST.get('id.foto')}';")
                
    except Exception as e:
        print(e)
