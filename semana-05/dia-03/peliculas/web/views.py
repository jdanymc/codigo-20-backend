from django.shortcuts import render
from .models import Pelicula

# Create your views here.
def index(request):
    lista_peliculas = Pelicula.objects.all()
    context = {
        'peliculas': lista_peliculas,
    }
    return render(request, 'index.html',context)