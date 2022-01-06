from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.

def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')


def buscar(request):


    if request.GET["prd"]:
        # mensaje = f"Articulo buscado : ", request.GET["prd"]
        producto = request.GET["prd"]

        if len(producto) > 20:
            mensaje =  "Demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains =  producto)
            return render(request, "resultados_busqueda.html", {"articulos" : articulos, "query": producto})


    else:
        mensaje = "Vacio"
    # mensaje = request.GET["prd"]
    return HttpResponse(mensaje)

def contacto(request):
    if request.method == "POST":
        return render(request, 'gracias.html')
    return render(request, 'contacto.html')