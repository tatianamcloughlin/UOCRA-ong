from django.shortcuts import render
from apps.noticias.models import Noticias,Categorias
from apps.cursos.models import Cursos
from apps.usuario.models import Usuario
from UOCRAong.sesion import login
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.db import connection

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

def formulario (request): 

    if request.POST.get('nombre_formulario')!=None:
        print(request.POST.get('nombre_formulario'))
        try:

            #(`password`, `last_login`, `email`, `fecha`, `usuario_activo`, `es_admin`, `apellido`, `direccion`, `dni`, `nombre`, `ciudad`, `cuil`, `provincia`, `usuario`)
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO `usuario_usuario` (`password`, `last_login`, `email`, `fecha`, `usuario_activo`, `es_admin`, `apellido`, `direccion`, `dni`, `nombre`, `ciudad`, `cuil`, `provincia`, `usuario`,`restablecer`) VALUES ('{make_password(request.POST.get('password1'))}', NULL , '{request.POST.get('email')}', '{datetime.now()}', '0', '0', '{request.POST.get('apellido')}', '{request.POST.get('direccion')}', '{request.POST.get('dni')}', '{request.POST.get('nombre_formulario')}', '{request.POST.get('ciudad')}', '{request.POST.get('dni')}', '{request.POST.get('provincia')}', '{request.POST.get('usuario')}',0)")
                
                row = cursor.fetchone()
        except Exception as e:
            print(e)
    


    
    return render(request, 'formulario.html')

def bienvenida (request): 

    if request.POST.get('nombre_formulario')!=None:
        mensaje_formulario = ''
        print(request.POST.get('nombre_formulario'))
        try:

            #(`password`, `last_login`, `email`, `fecha`, `usuario_activo`, `es_admin`, `apellido`, `direccion`, `dni`, `nombre`, `ciudad`, `cuil`, `provincia`, `usuario`)
            #with connection.cursor() as cursor:
                #cursor.execute(f"INSERT INTO `usuario_usuario` (`password`, `last_login`, `email`, `fecha`, `usuario_activo`, `es_admin`, `apellido`, `direccion`, `dni`, `nombre`, `ciudad`, `cuil`, `provincia`, `usuario`,`restablecer`) VALUES
                # 
                #  ('{
                # make_password(request.POST.get('password1'))}',
                #  NULL , 
                # '{request.POST.get('email')}',
                #  '{datetime.now()}',
                #  '0',
                #  '0',
                #  '{request.POST.get('apellido')}',
                #  '{request.POST.get('direccion')}',
                #  '{request.POST.get('dni')}',
                #  '{request.POST.get('nombre_formulario')}',
                #  '{request.POST.get('ciudad')}',
                #  '{request.POST.get('dni')}',
                #  '{request.POST.get('provincia')}',
                #  '{request.POST.get('usuario')}',
                # '0')")
            insertar = Usuario()
            insertar.nombre = request.POST.get('nombre_formulario')
            insertar.apellido= request.POST.get('apellido')
            insertar.email=request.POST.get('email')
            insertar.password=make_password(request.POST.get('password1'))
            insertar.provincia=request.POST.get('provincia')
            insertar.ciudad=request.POST.get('ciudad')
            insertar.dni=request.POST.get('dni')
            insertar.cuil=request.POST.get('cuil')
            insertar.usuario=request.POST.get('usuario')
            insertar.direccion=request.POST.get('direccion')
            insertar.fecha= datetime.now()
            insertar.usuario_activo=True
            insertar.restablecer=False
            insertar.es_admin=False
            insertar.save()
          
            
            
           

           
                
                #row = cursor.fetchone()
        except BaseException as e:
            mensaje_formulario = e.args[0]
            
        if mensaje_formulario == 1062:
                mensaje_formulario = 'El email ingresado ya se encuentra registrado'
                validar_registro = 1
        else:
            validar_registro = 0
      
    return render(request, 'bienvenida.html', {'mensaje_formulario':mensaje_formulario, 'validar_registro':validar_registro,})

