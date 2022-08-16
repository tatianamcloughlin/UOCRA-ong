from sqlite3 import Cursor
from django.shortcuts import render
from apps.cursos.models import Cursos , Galeria
from apps.noticias.models import Categorias
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from UOCRAong.sesion import login



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
    success_url= reverse_lazy ('cursos/cursos/galeria.html')



def ListaFotosPorCurso(request, nombre):
    curso= Cursos.objects.get(nombre=nombre)
    curso1 = Cursos.objects.filter (nombre=nombre)
    foto = Galeria.objects.filter(curso = curso1[0].id)  
    cursos = Cursos.objects.all()
    categorias= Categorias.objects.all()
    contexto = login(request)
    contexto['foto'] = foto
    contexto['cursos']= cursos
    contexto['categoria'] = categorias
    contexto['curso'] = curso

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
