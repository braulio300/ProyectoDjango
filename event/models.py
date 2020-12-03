from django.db import models

# Create your models here.
class Evento(models.Model):
    title      = models.CharField(max_length=100, verbose_name="Titulo")
    description= models.TextField(verbose_name="Descripción")
    image      = models.ImageField(verbose_name="Imagen", upload_to="Imagen Eventos")
    link       = models.URLField(verbose_name="Direccion Web",null=True, blank=True)
    created    = models.DateTimeField(auto_now_add=True,verbose_name="Creación")
    updated    = models.DateTimeField(auto_now=True,verbose_name="Actualización")
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural ="Eventos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
