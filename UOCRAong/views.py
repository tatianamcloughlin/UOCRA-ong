from django.shortcuts import render
from apps.noticias.models import Noticias
from apps.categoria.models import Categorias
def index(request):
    noticia = Noticias.objects.all()[:3]
    categoria = Categorias.objects.all()
    return render(request, 'index.html',{'noticia':noticia,'categoria':categoria})