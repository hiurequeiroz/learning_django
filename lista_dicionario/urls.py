from django.urls import path
from . import views

urlpatterns = [
    path('ordenar_numeros/', views.ordenar_numeros_view, name='ordenar_numeros'),
    path('contar_palavras/', views.contar_palavras_view, name='contar_palavras'),
]