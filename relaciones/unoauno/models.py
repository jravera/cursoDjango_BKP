from django.db import models

class Place(models.Model):

    name   = models.CharField( default = "" , max_length=50 )
    adress = models.CharField( default = "" , max_length=80 )

    def __str__(self):
        return self.name

class Restaurante(models.Model):
    
    place          = models.OneToOneField( Place, on_delete = models.CASCADE, primary_key = True )
    numOfEmployees = models.IntegerField( default = 1 )

    def __str__(self):
        return self.place.name
