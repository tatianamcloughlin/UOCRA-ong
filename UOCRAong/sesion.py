
from apps.noticias.models import Noticias
from django.contrib.auth.hashers import check_password


def login(request):      
    """Es para validar al inicar si hay datos post"""
    try:
        if request.POST.get('cerrar')==1:
            validacion = 0
            usuario = ""
            password = ""
            del request.session['usuario']
            del request.session['password']

        elif request.POST.get('cerrar') == 0:

            usuario=request.session['usuario']
            password=request.session['password']

        else:
            validacion = 0
            usuario = ""
            password = ""


        if request.session['validacion']:
            if request.session['validacion']==1:
                validacion= 1
                usuario=request.session['usuario']
                password=request.session['password']
            if request.POST.get('cerrar'):
                validacion = 0
                usuario = ""
                password = ""
                del request.session['usuario']
                del request.session['password']
                
    except Exception as e:
        validacion = 0
        usuario = ""
        password = ""

    
    if request.POST.get('usuario') and request.POST.get('password'):
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
    

            
    datos_usuario = Noticias.objects.raw("SELECT id,email,nombre, apellido, direccion,password, dni FROM `usuario_myuser` WHERE email='{}'".format(usuario))
    
    try:
        
        if check_password(password,datos_usuario[0].password):
            request.session['validacion'] = 1
            request.session['usuario'] = usuario
            request.session['password'] = password
            validacion = 1
            mensaje="Bienvenido {}".format(datos_usuario[0].email)
           
            
        elif datos_usuario[0].email!=usuario:
            request.session['validacion'] = 0
            mensaje="Email incorrecto"
        else:
            request.session['validacion'] = 0
            mensaje="contraseña incorrecta"
    except Exception as e:
        request.session['validacion'] = 0
        mensaje =usuario
        try:
            print(mensaje[0].email)
        except Exception as e:
            mensaje = "nada"
            
    return {'usuario': datos_usuario,'mensaje':mensaje,'validacion':validacion}