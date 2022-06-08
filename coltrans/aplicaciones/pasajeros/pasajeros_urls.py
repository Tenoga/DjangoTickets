from django.urls import path
from aplicaciones.pasajeros.views  import index, pasajeros_create, pasajeros_index, pasajeros_edit, pasajeros_delete, pasajeros_show

urlpatterns = [
    path('', index, name = "index"),
    path('pasajeros_create', pasajeros_create, name = "pasajeros_create"),
    path('pasajeros_show/<int:cod>/', pasajeros_show, name = "pasajeros_show"),
    path('pasajeros_edit/<int:cod>/', pasajeros_edit, name = "pasajeros_edit"),
    path('pasajeros_delete/<int:cod>/', pasajeros_delete, name = "pasajeros_delete"),
    path('pasajeros_index', pasajeros_index, name = "pasajeros_index"),
]