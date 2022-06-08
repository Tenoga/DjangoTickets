# from django.db import models
# from aplicaciones.routes.models import Route
# from aplicaciones.buses.models import Bus
# from aplicaciones.pasajeros.models import Pasajero

# class Ticket(models.Model):
#     id = models.AutoField(primary_key = True)
#     route_id = models.ForeignKey( Route, on_delete=models.CASCADE)
#     bus_id = models.ForeignKey( Bus, on_delete=models.CASCADE)
#     pasajero_id = models.ForeignKey( Pasajero, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     travel_date = models.DateField()
#     departure_time = models.TimeField()
