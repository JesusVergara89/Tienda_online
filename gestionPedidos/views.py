from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulos

# Create your views here.

def busqueda_productos(request):
    return render(request, "Busqueda_productos.html")

def buscar(request):
    if request.GET["producto"]:
        #mensaje= "Articulo buscado: {}".format(request.GET["producto"])
        product=request.GET["producto"]
        if len(product) > 20:
            mensaje="Texto de busqueda demasiado largo"
        else:
            Articulos=articulos.objects.filter(nombre__icontains=product)
            return render(request, "resultados_busqueda.html", {"articulos":Articulos, "query": product})
    else:
        mensaje= "No has introducido nada"
    return HttpResponse(mensaje)