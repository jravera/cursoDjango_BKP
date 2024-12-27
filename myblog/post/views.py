from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor, Entry



def queries(request):

    # Obtengo todos los autores
    autores = Autor.objects.all()
    
    # Obtengo los autores filtrados por condicion
    filtrados = Autor.objects.filter(email='amylove@example.com')
                                     
    # Obtengo un unico objeto filtrado
    unautor = Autor.objects.get(id=25)

    # Obtengo los 10 primeros valores [0:10] -> [offset:limit]
    rangoLimit = Autor.objects.all()[:10]

    # Obtengo los 10 primeros valores [5:10] -> [offset:limit]
    rangoOffset = Autor.objects.all()[5:10]

    # Ordeno los autores por email
    autoresXEmail = Autor.objects.all().order_by('email')

    # Obtengo todos los elementos con id <= 15
    idMenorA15 = Autor.objects.filter(id__lte = 15)

    # Otras opciones (nombreDelCampo__xxx)
    # __lte      : lower than equal   <=
    # __gte      : greater than equal >=
    # __lt       : lower than
    # __gt       : greater than
    # __contains : contiene
    # __exact    : exacto

    # Obtengo todos los autores cuyo nombre contiene 'yes'
    nameHasYes = Autor.objects.filter(name__contains = 'yes')


    return render(request, 'post/queries.html',
                 { 'autores':autores, 'filtrados':filtrados, 'unautor':unautor, 'rangoLimit':rangoLimit, 
                   'rangoOffset':rangoOffset, 'autoresXEmail':autoresXEmail, 'idMenorA15': idMenorA15, 'nameHasYes':nameHasYes })
