from django.urls import path
from . import views

urlpatterns = [
    path('inverter_palavra/', views.inverter_palavra_view, name='inverter_palavra')
]