# main/views.py
from django.shortcuts import render

def index(request):
    modelos = [
        {'nombre': 'Modelo Básico', 'descripcion': 'Descripción del modelo básico.'},
        {'nombre': 'Modelo Premier', 'descripcion': 'Descripción del modelo premier.'},
        {'nombre': 'Modelo Elite', 'descripcion': 'Descripción del modelo elite.'},
    ]
    
    servicios = [
        {'titulo': 'Diseño Personalizado', 'descripcion': 'Diseño de casas a medida según tus preferencias.', 'precio': '$20,000'},
        {'titulo': 'Construcción Ecológica', 'descripcion': 'Construcción con materiales sostenibles y ecológicos.', 'precio': '$30,000'},
        {'titulo': 'Asesoría en Decoración', 'descripcion': 'Asesoría para la decoración de tu nuevo hogar.', 'precio': '$5,000'},
    ]

    contexto = {'modelos': modelos, 'servicios': servicios}
    return render(request, 'main/index.html', contexto)


def contacto(request):
    return render(request, 'main/contacto.html')

def galeria(request):
    return render(request, 'main/galeria.html')
