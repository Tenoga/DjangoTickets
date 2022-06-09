from django.db import models
from aplicaciones.rutas.models import Ruta
from aplicaciones.buses.models import Bus
from aplicaciones.pasajeros.models import Pasajero

class Tiquetes(models.Model):
    id = models.AutoField(primary_key = True)
    ruta = models.ForeignKey( Ruta, on_delete=models.CASCADE)
    bus = models.ForeignKey( Bus, on_delete=models.CASCADE)
    pasajero = models.ForeignKey( Pasajero, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_viaje = models.DateField()
    hora_salida = models.TimeField()

    # def __str__(self):
    #     return self.origin