from django.shortcuts import render, redirect
from .models import Bus
from .forms import BusForm


# ----------Envia el objeto buses a la vista index-----------#

def buses_index(request):
    buses = Bus.objects.all()
    return render(request, "buses/buses_index.html", {'buses':buses})

# ----------Buses Create GET / POST-----------#

def buses_create(request):
    if(request.method == 'GET'):
        forms = BusForm()
        listado = {
            'form' : forms,
            'titulo': 'Registrar Bus',
            'boton': 'Registrar'
        }
    else:
        forms = BusForm(request.POST)
        listado = {
            'form': forms,
            'titulo': 'Registrar Bus',
            'boton': 'Registrar'
        }
        if forms.is_valid():
            forms.save()
            return redirect('buses_index')
    return render(request, "buses/buses_create.html", listado)

# ----------Buses EDIT-----------#

def buses_edit(request, cod):
    bus = Bus.objects.get( id = cod)
    if (request.method == 'GET'):
        form = BusForm(instance = bus)
        listado = {
            'form': form,
            'titulo': 'Editar Bus',
            'tipo': bus.tipo,
            'placa': bus.placa,
            'capacidad': bus.capacidad,
            'compañia': bus.compañia,
            'boton': 'Guardar'
        }
    else:
        forms = BusForm(request.POST, instance = bus)
        listado = {
            'form': forms
        }
        if forms.is_valid():
            forms.save()
            return redirect('buses_index')
    return render(request, 'buses/buses_create.html', listado)

# ----------Buses DELETE-----------#

def buses_delete(request, cod):
    bus = Bus.objects.get(id = cod)
    bus.delete()
    return redirect('buses_index')

# ----------Buses Show-----------#
def buses_show(request, cod):
    bus = Bus.objects.get(id = cod)
    return render(request, "buses/buses_show.html", {'buses':bus})