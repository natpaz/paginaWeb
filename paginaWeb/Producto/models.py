from django.db import models

# Create your models here.
class Producto (models.Model):
    
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=7)
    imagen = models.ImageField(upload_to='img')
 
    def __str__(self):
        return str(self.imagen)
