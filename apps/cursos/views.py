from django.shortcuts import render
from apps.cursos.models import Cursos , Galeria
from apps.noticias.models import Categorias
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView



def curso (request, nombre ):
    curso2= Cursos.objects.get(nombre=nombre)
    categorias= Categorias.objects.all()
    cursos = Cursos.objects.all()
    return render(request, 'cursos/basecursos.html',{'curso':curso2,'categoria':categorias, 'cursos': cursos})



class addFotos(CreateView):
    model= Galeria
    fields=['curso','imagen','activo' ]
    template_name = 'cursos/addFotos.html'
    success_url= reverse_lazy ('index')



def ListaFotosPorCurso(request, curso):
    curso = Cursos.objects.filter(nombre=curso)
    foto = Galeria.objects.filter(curso = curso[0].id)  
    cursos = Cursos.objects.all()
    categorias= Categorias.objects.all()
    return render(request,'cursos/galeria.html', {'foto':foto, 'cursos':cursos,'categoria':categorias })


def MostrarGaleria(request):
    foto = Galeria.objects.all()    
    cursos = Cursos.objects.all()
    categorias= Categorias.objects.all()
    context = {'foto': foto,'cursos':cursos,'categoria':categorias}
  
    return render (request, 'cursos/galeria.html', context)





# Create your views here.
