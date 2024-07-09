from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import contar_form
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

def contacto(request):
    if request.method=="POST":
       miFormulario=contar_form(request.POST)
       if miFormulario.is_valid():
           infForm=miFormulario.cleaned_data
           send_mail(infForm['asunto'], infForm['mensaje'],'ingenierocivil.jmm@outlook.com',[infForm.get('email'),'ingenierocivil.jmm@outlook.com'],)
           return render(request, "gracias.html")
    else:
        miFormulario=contar_form()    
    return render(request, "form_contacto.html", {"form":miFormulario})
           

    #if request.method=="POST":
        #subject=request.POST["asunto"]
        #message=request.POST["mensaje"] + " " + request.POST["email"]
        #email_from=settings.EMAIL_HOST_USER
        #recipient_list=["jesusmanuelitsa1989@gmail.com"]
        #send_mail(subject, message, email_from, recipient_list)
        #return render(request, "gracias.html")
    #return render(request, "contacto.html")





