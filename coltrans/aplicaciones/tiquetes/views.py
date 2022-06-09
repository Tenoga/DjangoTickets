from django.shortcuts import render, redirect
from .models import Tiquetes
from .forms import TiqueteForm


# ----------Envia el objeto tiquetes a la vista index-----------#

def tiquetes_index(request):
    tiquetes = Tiquetes.objects.all()
    return render(request, "tiquetes/tiquetes_index.html", {'tiquetes':tiquetes})

# ----------Tiquetes Create GET / POST-----------#

def tiquetes_create(request):
    if(request.method == 'GET'):
        forms = TiqueteForm()
        listado = {
            'form' : forms,
            'titulo': 'Registrar Tiquete',
            'boton': 'Registrar'
        }
    else:
        forms = TiqueteForm(request.POST)
        listado = {
            'form': forms,
            'titulo': 'Registrar Tiquete',
            'boton': 'Registrar'
        }
        if forms.is_valid():
            forms.save()
            return redirect('tiquetes_index')
    return render(request, "tiquetes/tiquetes_create.html", listado)

# ----------Tiquetes EDIT-----------#

def tiquetes_edit(request, cod):
    tiquete = Tiquetes.objects.get( id = cod)
    if (request.method == 'GET'):
        form = TiqueteForm(instance = tiquete)
        listado = {
            'form': form,
            'titulo': 'Editar Tiquete',
            'ruta_id': tiquete.ruta_id,
            'bus_id': tiquete.bus_id,
            'pasajero_id': tiquete.pasajero_id,
            'cantidad': tiquete.cantidad,
            'fecha_viaje': tiquete.fecha_viaje,
            'hora_salida': tiquete.hora_salida,
            'boton': 'Guardar'
        }
    else:
        forms = TiqueteForm(request.POST, instance = tiquete)
        listado = {
            'form': forms
        }
        if forms.is_valid():
            forms.save()
            return redirect('tiquetes_index')
    return render(request, 'tiquetes/tiquetes_create.html', listado)

# ----------Tiquetes DELETE-----------#

def tiquetes_delete(request, cod):
    tiquete = Tiquetes.objects.get(id = cod)
    tiquete.delete()
    return redirect('tiquetes_index')

# ----------Tiquetes Show-----------#
def tiquetes_show(request, cod):
    tiquete = Tiquetes.objects.get(id = cod)
    return render(request, "tiquetes/tiquetes_show.html", {'tiquetes':tiquete})