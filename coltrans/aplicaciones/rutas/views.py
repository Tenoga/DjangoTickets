from django.shortcuts import render, redirect
from .models import Ruta
from .forms import RutaForm


# ----------Envia el objeto ruta a la vista index-----------#

def rutas_index(request):
    rutas = Ruta.objects.all()
    return render(request, "rutas/rutas_index.html", {'rutas':rutas})

# ----------Rutas Create GET / POST-----------#

def rutas_create(request):
    if(request.method == 'GET'):
        forms = RutaForm()
        listado = {
            'form' : forms,
            'titulo': 'Registrar Ruta',
            'boton': 'Registrar'
        }
    else:
        forms = RutaForm(request.POST)
        listado = {
            'form': forms,
            'titulo': 'Registrar Ruta',
            'boton': 'Registrar'
        }
        if forms.is_valid():
            forms.save()
            return redirect('rutas_index')
    return render(request, "rutas/rutas_create.html", listado)

# ----------Rutas EDIT-----------#

def rutas_edit(request, cod):
    ruta = Ruta.objects.get( id = cod)
    if (request.method == 'GET'):
        form = RutaForm(instance = ruta)
        listado = {
            'form': form,
            'titulo': 'Editar ruta',
            'origen': ruta.origen,
            'destino': ruta.destino,
            'boton': 'Guardar'
        }
    else:
        forms = RutaForm(request.POST, instance = ruta)
        listado = {
            'form': forms
        }
        if forms.is_valid():
            forms.save()
            return redirect('rutas_index')
    return render(request, 'rutas/rutas_create.html', listado)

# ----------Rutas DELETE-----------#

def rutas_delete(request, cod):
    ruta = Ruta.objects.get(id = cod)
    ruta.delete()
    return redirect('rutas_index')

# ----------Rutas Show-----------#
def rutas_show(request, cod):
    ruta = Ruta.objects.get(id = cod)
    return render(request, "rutas/rutas_show.html", {'rutas':ruta})