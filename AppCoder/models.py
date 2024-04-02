from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=48)
    camada = models.IntegerField()
    nivel = models.CharField(max_length=20)