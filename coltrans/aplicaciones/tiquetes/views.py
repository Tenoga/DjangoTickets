from django.shortcuts import render



def index(request):
    return render(request, "tiquetes/index.html", {})

# ----------Tiquetes-----------#

def tiquetes_create(request):
    return render(request, "tiquetes/tiquetes_create.html", {})
# Create your views here.
