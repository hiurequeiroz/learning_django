from django.urls import path
from . import views

urlpatterns = [
    path('verifica_paridade/', views.verifica_paridade, name='verifica_paridade')
]