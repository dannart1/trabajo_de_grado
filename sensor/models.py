from django.db import models

# Create your models here.
class sensor(models.Model):
    id = models.AutoField(primary_key=True, default=-1, unique=True, null=False, blank=False)
    IDSensor = models.TextField()
    Fecha = models.DateField()
    Hora = models.DurationField()
    Temperatura = models.TextField()
    Humedad = models.TextField()