from django.urls import path
from . import views

urlpatterns = [
    path('verificar_palindromo/', views.verificar_palindromo_view, name='verificar_palindromo'),
]