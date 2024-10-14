# main/urls.py
from django.urls import path
from .views import index, contacto, galeria

urlpatterns = [
    path('', index, name='index'),  # URL para la vista de índice
    path('contacto/', contacto, name='contacto'),  # URL para la vista de contacto
    path('galeria/', galeria, name='galeria'),  # URL para la vista de galería
]
