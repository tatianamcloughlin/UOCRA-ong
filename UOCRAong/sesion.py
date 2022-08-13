from apps.noticias.models import Noticia
from django.contrib.auth.hashers import check_password


def login(request):      
    
    usuario = request.POST.get('usuario')
    password = request.POST.get('password')
    validacion = request.POST.get('cerrar')
    
    if request.POST.get('cerrar'):
        validacion = request.POST.get('cerrar')
        
    else:
        if request.session['validacion']:
            validacion = request.session['validacion'] = 1
        else:
            validacion = "1"
        
        
    
    if validacion == "1":
        usuario = request.POST.get('usuario',None)
        password = request.POST.get('password',None)
        request.session['usuario'] = None
        request.session['password'] = None
        mensaje ="registrse"
        request.session['validacion'] = 0
    else:
        if request.session['validacion'] == 1:
            
            usuario = request.session['usuario']
            password = request.session['password']
            
    datos_usuario = Noticia.objects.raw("SELECT * FROM auth_user WHERE email='{}'".format(usuario))
    
    try:
        
        if check_password(password,datos_usuario[0].password):
            request.session['validacion'] = 1
            request.session['usuario'] = usuario
            request.session['password'] = password
            validacion = 1
            mensaje="Bienvenido {}".format(datos_usuario[0].username)
           
            
        elif datos_usuario[0].email!=usuario:
            request.session['validacion'] = 0
            mensaje="Email incorrecto"
        else:
            request.session['validacion'] = 0
            mensaje="contraseña incorrecta"
    except Exception as e:
        request.session['validacion'] = 0
        mensaje ="Email incorrecto"
            
    return {'usuario': datos_usuario,'mensaje':mensaje,'validacion':validacion}