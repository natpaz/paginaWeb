from django.db import models

# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()
 
    def __str__(self):
        return self.nombre