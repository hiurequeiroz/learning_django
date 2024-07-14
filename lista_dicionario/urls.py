from django.urls import path
from . import views

urlpatterns = [
    path('ordenar_numeros/', views.ordenar_numeros_view, name='ordenar_numeros'),
]