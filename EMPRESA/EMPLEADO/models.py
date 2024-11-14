from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):  
    nombre_usuario = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(max_length=254, unique=True)
    contraseña = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto_aplicado = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.nombre} {self.apellido} - {self.puesto_aplicado}"