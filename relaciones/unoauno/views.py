from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurante


def create(request):
    place       = Place( name = 'Lugar 1', adress = 'Direccion 1' )
    place.save()

    restaurante = Restaurante( place = place, numOfEmployees = 8 )
    restaurante.save()

    return HttpResponse( 'Restaurante: ' + restaurante.place.name )
