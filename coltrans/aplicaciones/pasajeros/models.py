from django.db import models

class Pasajero (models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField( max_length= 80)
    apellido = models.CharField( max_length= 80)
    cedula = models.CharField( max_length= 80, unique = True)
    correo = models.EmailField( max_length= 120, unique = True)
    telefono = models.CharField( max_length= 80)
