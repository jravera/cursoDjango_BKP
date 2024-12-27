from django.shortcuts import render
from django.http      import HttpResponse
from .models import comments

def test(request):
    return HttpResponse('hola que tal, funciona correctamente') 

def create(request):

    # Primer forma de guardar un objeto
    # ---------------------------------
    #comentario = comments(name='juanjo',score=5, comment='Esto es un comentario')
    #comentario.save()
    
    # Segunda forma de guardado (no necesita el 'save()' del ejemplo anterior)
    # ------------------------------------------------------------------------
    comentario = comments.objects.create(name='otro nombre')

    return HttpResponse('Ruta para el alta de datos en el modelo')

def delete(request):

    # Primera forma de borrado
    # ------------------------
    
    # Para borrar primero localizo el objeto a borrar
    #comentario = comments.objects.get(id=1)

    #nombre = comentario.name

    # Luego de localizado lo borro
    #comentario.delete()
    #return HttpResponse('Borrado el registro de: ' + nombre )

    # Segunda forma de borrado
    # ------------------------
    # Ojo aca xq si el filtro no es por la prymaryKey se pueden borrar mas de un registro
    comments.objects.filter(id=2).delete()
    return HttpResponse('Segundo ejemplo de borrado de registro' )