from django.urls import path
from aplicaciones.tiquetes.views  import index, tiquetes_create

urlpatterns = [
    path('', index, name = "index"),
    path('tiquetes_create', tiquetes_create, name = "tiquetes_create"),

]