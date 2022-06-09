from django.db import models
from aplicaciones.rutas.models import Ruta
from aplicaciones.buses.models import Bus
from aplicaciones.pasajeros.models import Pasajero

class Tiquetes(models.Model):
    id = models.AutoField(primary_key = True)
    ruta_id = models.ForeignKey( Ruta, on_delete=models.CASCADE)
    bus_id = models.ForeignKey( Bus, on_delete=models.CASCADE)
    pasajero_id = models.ForeignKey( Pasajero, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_viaje = models.DateField()
    hora_salida = models.TimeField()
