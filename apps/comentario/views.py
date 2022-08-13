from multiprocessing import context
from django.shortcuts import render
from .forms import ComentarioForm
from .models import Comentario

# Create your views here.
def AddComentario(request):
	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	context={
		'form': form,
	}
	return render(request,'comentario/addcomentario.html', context)

def Comentarios(request):
    comentario = Comentario.objects.all() 
    context = {'comentario':comentario,}
    return render(request, 'comentario/listarcomentario.html', context)
