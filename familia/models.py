from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    mayor_de_edad = models.BooleanField()
    parentesco = models.CharField(max_length=20)
     