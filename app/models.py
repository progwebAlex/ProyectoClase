from django.db import models

# Create your models here.
class Cliente(models.Model):
    Nombre=models.CharField(max_length=50)
    Edad=models.CharField(max_length=20)
    Telefono=models.CharField(max_length=10)

class Vuelo(models.Model):
    capacidad=models.CharField(max_length=50)
    modeloAvion=models.CharField(max_length=50)
    numeroVuelo=models.CharField(max_length=50)
    compañia=models.ForeignKey(Compañia)


class Pasaje(models.Model):
    clase=models.CharField(max_length=50)
    asiento=models.CharField(max_length=50)
    valor=models.IntegerField
    cliente=models.ForeignKey(Cliente)
    vuelo=models.ForeignKey(Vuelo)

