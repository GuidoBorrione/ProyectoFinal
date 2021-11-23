from django.core.files.utils import FileProxyMixin
from django.urls import path
from django.urls.resolvers import URLPattern
from.views import Home, crearAparato
from.forms import AparatoForm
from django.shortcuts import redirect, render


urlpatterns = [
    path('',Home, name='Aparato_Form'),
    path('crear_Aparato/', crearAparato, name= 'Aparato_Form'),
]