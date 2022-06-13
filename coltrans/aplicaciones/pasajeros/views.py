from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pasajero
from .forms import PasajeroForm

# ----------INDEX-----------#
def index(request):
    return render(request, "index.html", {})

# ----------Envia el objeto pasajeros a la vista index-----------#

def pasajeros_index(request):
    pasajero = Pasajero.objects.all()
    return render(request, "pasajeros/pasajeros_index.html", {'pasajeros':pasajero})


# ----------Pasajeros Create GET / POST-----------#

def pasajeros_create(request):
    if(request.method == 'GET'):
        forms = PasajeroForm()
        listado = {
            'form' : forms,
            'titulo': 'Crear Pasajero',
            'boton': 'Crear'
        }
    else:
        forms = PasajeroForm(request.POST)
        listado = {
            'form': forms,
            'titulo': 'Crear Pasajero',
            'boton': 'Crear'
        }
        if forms.is_valid():
            forms.save()
            return redirect('pasajeros_index')
    return render(request, "pasajeros/pasajeros_create.html", listado)



# ----------Pasajeros EDIT-----------#
def pasajeros_edit(request, cod):
    pasajero = Pasajero.objects.get( id = cod)
    if (request.method == 'GET'):
        form = PasajeroForm(instance = pasajero)
        listado = {
            'form': form,
            'titulo': 'Editar Pasajero',
            'nombre': pasajero.nombre,
            'apellido': pasajero.apellido,
            'correo': pasajero.correo,
            'cedula': pasajero.cedula,
            'telefono': pasajero.telefono,
            'boton': 'Guardar'
        }
    else:
        forms = PasajeroForm(request.POST, instance = pasajero)
        listado = {
            'form': forms
        }
        if forms.is_valid():
            forms.save()
            return redirect('pasajeros_index')
    return render(request, 'pasajeros/pasajeros_create.html', listado)

# ----------Pasajeros DELETE-----------#

def pasajeros_delete(request, cod):
    pasajero = Pasajero.objects.get(id = cod)
    pasajero.delete()
    return redirect('pasajeros_index')

# ----------Pasajeros Show-----------#
def pasajeros_show(request, cod):
    pasajero = Pasajero.objects.get(id = cod)
    return render(request, "pasajeros/pasajeros_show.html", {'pasajero':pasajero})
