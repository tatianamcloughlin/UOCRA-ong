from django.shortcuts import render
from apps.noticias.models import Noticias,Categorias
from apps.cursos.models import Cursos
from UOCRAong.sesion import login
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.db import connection

def inicio(request):
    noticia = Noticias.objects.all().order_by('-fecha')[:3]
    categoria = Categorias.objects.all()
    cursos = Cursos.objects.all()
    contexto = login(request)
    contexto['noticia'] = noticia
    contexto['categoria'] = categoria
    contexto['cursos'] = cursos
    

    return render(request, 'inicio.html',contexto)


def index (request):
    return render(request, 'index.html')

def formulario (request): 

    if request.POST.get('nombre_formulario')!=None:
        print(request.POST.get('nombre_formulario'))
        try:

            #(`password`, `last_login`, `email`, `fecha`, `usuario_activo`, `es_admin`, `apellido`, `direccion`, `dni`, `nombre`, `ciudad`, `cuil`, `provincia`, `usuario`)
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO `usuario_myuser` (`password`, `last_login`, `email`, `fecha`, `usuario_activo`, `es_admin`, `apellido`, `direccion`, `dni`, `nombre`, `ciudad`, `cuil`, `provincia`, `usuario`) VALUES ('{make_password(request.POST.get('password1'))}', '', '{request.POST.get('email')}', '{datetime.now()}', '0', '0', '{request.POST.get('apellido')}', '{request.POST.get('direccion')}', '{request.POST.get('dni')}', '{request.POST.get('nombre_formulario')}', '{request.POST.get('ciudad')}', '{request.POST.get('dni')}', '{request.POST.get('provincia')}', '{request.POST.get('usuario')}')")
                
                row = cursor.fetchone()
        except Exception as e:
            print(e)
    


    
    return render(request, 'formulario.html')