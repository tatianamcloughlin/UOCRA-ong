from multiprocessing import context
from sqlite3 import Cursor
from django.shortcuts import render
from apps.cursos.models import Cursos , Galeria
from apps.noticias.models import Categorias
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from UOCRAong.sesion import login
from apps.usuario.models import UsuarioManager

from django.db import connection


def curso (request, nombre ):
    curso2= Cursos.objects.get(nombre=nombre)
    categorias= Categorias.objects.all()
    cursos = Cursos.objects.all()
    contexto = login(request)
    contexto['curso'] = curso2
    contexto['categoria'] = categorias
    contexto['cursos'] = cursos
    return render(request, 'cursos/basecursos.html', contexto)



class addFotos(CreateView):
    model= Galeria
    fields=['curso','imagen','activo' ]
    template_name = 'cursos/addFotos.html'
    success_url= reverse_lazy ('apps.cursos:galeria')



def ListaFotosPorCurso(request, nombre):
    curso= Cursos.objects.get(nombre=nombre)
    foto = Galeria.objects.filter(curso=curso)  
    cursos = Cursos.objects.all()
    categorias= Categorias.objects.all()
    contexto = login(request)
    contexto['foto'] = foto
    contexto['cursos']= cursos
    contexto['categoria'] = categorias
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
    curso = Cursos.objects.all()
    categorias= Categorias.objects.all()
    

    
    contexto = login(request)
    contexto['foto'] = foto
    contexto['cursos'] = curso
    contexto['categoria'] = categorias
    
  
    return render (request, 'cursos/galeriaGeneral.html', contexto)





# Create your views here.
def EliminarFoto (request): 
    foto = Galeria.objects.all()    
    curso = Cursos.objects.all()
    categorias= Categorias.objects.all()
    
    contexto = login(request)
    contexto['foto'] = foto
    contexto['cursos'] = curso
    contexto['categoria'] = categorias
    
    try:
        print(request.POST.get('id.foto'))
        with connection.cursor() as cursor:
               cursor.execute (f"DELETE FROM 'cursos_galeria' WHERE id='{request.POST.get('id.foto')}';")
                
    except Exception as e:
        print(e)
