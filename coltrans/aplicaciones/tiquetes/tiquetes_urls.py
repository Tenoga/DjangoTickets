from django.urls import path
from aplicaciones.tiquetes.views  import tiquetes_create, tiquetes_index, tiquetes_edit, tiquetes_delete, tiquetes_show

urlpatterns = [
    path('tiquetes_index', tiquetes_index, name = "tiquetes_index"),
    path('tiquetes_create', tiquetes_create, name = "tiquetes_create"),
    path('tiquetes_show/<int:cod>/', tiquetes_show, name = "tiquetes_show"),
    path('tiquetes_edit/<int:cod>/', tiquetes_edit, name = "tiquetes_edit"),
    path('tiquetes_delete/<int:cod>/', tiquetes_delete, name = "tiquetes_delete")
]