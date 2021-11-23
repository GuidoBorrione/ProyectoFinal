from django.shortcuts import render
from django.shortcuts import redirect
from.forms import AparatoForm
from.forms import ClaseForm
from.forms import EntrenadorForm
from.forms import ActividadForm
from.forms import SalaForm
from.forms import SocioForm
from.forms import Clase_SocioForm
from.forms import Entrenador_ActividadForm


def Home(request):
    return render(request, 'gimnacio/inicio.html')

def crearAparato(request):

    if request.method == 'POST':
        aparato_form = AparatoForm(request.POST)

        if AparatoForm.is_valid():
            aparato_form.save()
        return redirect('inicio')
    else:
        aparato_form = AparatoForm()
    return render(request, 'gimnacio/index.html',{'aparato_form': aparato_form})