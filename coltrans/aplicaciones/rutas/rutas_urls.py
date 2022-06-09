from django.urls import path
from aplicaciones.rutas.views  import rutas_create, rutas_index, rutas_edit, rutas_delete, rutas_show

urlpatterns = [
    path('rutas', rutas_index, name = "rutas_index"),
    path('rutas_create', rutas_create, name = "rutas_create"),
    path('rutas_show/<int:cod>/', rutas_show, name = "rutas_show"),
    path('rutas_edit/<int:cod>/', rutas_edit, name = "rutas_edit"),
    path('rutas_delete/<int:cod>/', rutas_delete, name = "rutas_delete"),
    
]