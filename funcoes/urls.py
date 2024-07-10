from django.urls import path
from . import views

urlpatterns = [
    path('somar_numeros', views.somar_numeros_view, name='somar_numeros'),
]