from django.urls import path
from aplicaciones.buses.views import buses_create, buses_index, buses_delete, buses_show, buses_edit

urlpatterns = [
    path('buses', buses_index, name = "buses_index"),
    path('buses_create', buses_create, name = "buses_create"),
    path('buses_show/<int:cod>/', buses_show, name = "buses_show"),
    path('buses_edit/<int:cod>/', buses_edit, name = "buses_edit"),
    path('buses_delete/<int:cod>/', buses_delete, name = "buses_delete"),
]