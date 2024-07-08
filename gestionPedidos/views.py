from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def busqueda_productos(request):
    return render(request, "Busqueda_productos.html")

def buscar(request):
    mensaje= "Articulo buscado: {}".format(request.GET["producto"])
    return HttpResponse(mensaje)