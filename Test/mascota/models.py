from django.db import models
from adopcion.models import Persona

# Create your models here.
class Vacuna(models.Model):
    name = models.CharField(max_length= 200, verbose_name ="Nombre")

class Mascota(models.Model):
    folio = models.CharField(primary_key= True, max_length = 200, verbose_name= "Folio")
    name  = models.CharField(max_length = 200, verbose_name= "Nombre")
    sex = models.CharField(max_length=10, verbose_name = "Sexo")
    age = models.IntegerField(verbose_name= "Edad")
    date_rescue = models.DateField(verbose_name = "Fecha de rescate")
    person = models.ForeignKey(Persona, null = True, blank = True, on_delete= models.CASCADE)
    vacun = models.ManyToManyField(Vacuna)
