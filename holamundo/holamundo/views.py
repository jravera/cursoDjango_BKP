from django.http import HttpResponse

def saludo(request):
    return HttpResponse('Hola Mundo')

def despedida(request):
    return HttpResponse('Hasta luegooooo')

def adulto(request, edad):
    if edad >= 18 :
        return HttpResponse('Eres ya mayor de edad')
    else:
        return HttpResponse('Aun eres un menor de edad')
    