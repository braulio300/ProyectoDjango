from django.db import models

# Create your models here.
class Boleta(models.Model):
    idBoleta        = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    total           = models.IntegerField()

    def __str__(self):
        return self.idBoleta

class Local(models.Model):
    idLocal         = models.DecimalField(max_digits=10, decimal_places=0,primary_key=True)
    direccionLocal  = models.CharField(max_length=100)
    encargadoLocal  = models.TextField(max_length=100)

    def __str__(self):
        return self.idLocal

class Produccion(models.Model):
    idProduccion    = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    fechaInicio     = models.DateField()
    horaInicio      = models.IntegerField()
    fechaFinal      = models.DateField()
    horaTermino     = models.IntegerField()
    lugarEvento     = models.CharField(max_length=30)
    invitados       = models.IntegerField()
    seguridad       = models.IntegerField()
    dj              = models.IntegerField()
    bartender       = models.IntegerField()

    def __str__(self):
        return self.idProduccion

class Staff(models.Model):
    rut            = models.DecimalField(max_digits=10, decimal_places=0)
    nombre         = models.CharField(max_length=30)
    apellido       = models.CharField(max_length=30)
    corre          = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre   