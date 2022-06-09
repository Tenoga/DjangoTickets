from django.db import models

class Bus(models.Model):
    id = models.AutoField(primary_key = True)
    tipo = models.CharField( max_length = 255 )
    placa = models.CharField( max_length = 10 )
    capacidad = models.SmallIntegerField()
    compañia = models.CharField( max_length = 255 )