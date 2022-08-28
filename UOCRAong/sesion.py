
from apps.usuario.models import Usuario
from django.contrib.auth.hashers import check_password,make_password


def login(request):      
    """Es para validar al inicar si hay datos post"""
    mensaje=""
    try:
        
        if request.POST.get('editar_password1'):
            password1 = request.POST.get('editar_password1')
            editar= Usuario.objects.get(email=request.session['usuario'])
            editar.password=make_password(password1)
            editar.save()
        
      
    except Exception as e:
        print(e)
            

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

        try:

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
            print(e)            
    

    
        if request.POST.get('usuario') and request.POST.get('password'):
            usuario = request.POST.get('usuario')
            password = request.POST.get('password')
    

        try:    
            datos_usuario = Usuario.objects.get(email=f"{usuario}")
            if check_password(password,datos_usuario.password):
                request.session['validacion'] = 1
                request.session['usuario'] = usuario
                request.session['password'] = password
                validacion = 1
                mensaje="Bienvenido {}".format(datos_usuario.email)

               
       
            else:
                validacion = 0
                try:
                    del request.session['usuario']
                    del request.session['password']
                except Exception as e:
                    print(e)
                    datos_usuario=[]       
                    mensaje="Contraseña Incorrecto"
        except Exception as e:
            try:
                validacion = 0
                del request.session['usuario']
                del request.session['password']
            except Exception as e:
                print(e)
                datos_usuario=[]       
                mensaje="Email Incorrecto"
    

    except Exception as e:
        validacion = 0
        usuario = ""
        password = ""
        try:
            del request.session['usuario']
            del request.session['password']
        except Exception as e:
            print(e)
        datos_usuario=""      
        mensaje="Algo salio mal"

        
    return {'usuario': datos_usuario,'mensaje':mensaje,'validacion':validacion}
