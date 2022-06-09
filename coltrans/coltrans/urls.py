from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicaciones.pasajeros.pasajeros_urls'), name="pasajeros_urls"),
    path('', include('aplicaciones.tiquetes.tiquetes_urls'), name="tiquetes"),
    path('', include('aplicaciones.buses.buses_urls'), name="buses"),
    path('', include('aplicaciones.rutas.rutas_urls'), name="rutas"),

]
