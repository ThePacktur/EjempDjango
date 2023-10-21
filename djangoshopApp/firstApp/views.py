from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def renderindex(request):
    return render(request, 'firstApp/index.html')

def productos(request):
    productos = [
        {'nombre': 'Producto 1', 'imagen': ''},
        {'nombre': 'Producto 2', 'imagen': ''},
        {'nombre': 'Producto 3', 'imagen': ''},
    ]
    return render(request, 'firstApp/productos.html', productos)
