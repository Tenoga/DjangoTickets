from django.db import models

class Ruta(models.Model):
    id = models.AutoField(primary_key = True)
    origen = models.CharField( max_length = 255 )
    destino = models.CharField( max_length = 255 )

    def __str__(self):
        data = f"{self.origen} -> {self.destino}"
        return data