from django.db import models

# Create your models here.
class Persona(models.Model):
    name  = models.CharField(max_length = 200, verbose_name= "Nombre")
    lastname = models.CharField(max_length = 200, verbose_name= "Apellidos")
    age = models.IntegerField(verbose_name= "Edad")
    phone = models.CharField(max_length = 200, verbose_name= "Teléfono")
    email = models.EmailField(verbose_name= "Correo")
    address = models.TextField(verbose_name= "Dirección")
