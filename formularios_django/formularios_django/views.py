from django.shortcuts import render
from django.http      import HttpResponse
from .forms           import CommentForm

def form(request):
    comment_form = CommentForm({'name':'Federico', 'url':'http://google.com','comment':'comentario'})
    return render(request, 'form.html' , {'comment_form':comment_form})

def goal(request):
    # if request.method != 'GET':   (SOLUCION CON GET)
    if request.method != 'POST':  # (SOLUCION CON POST)
        return HttpResponse('Metodo no permitido')
    
    #return HttpResponse('nombre:'+ request.GET['name'])   (SOLUCION CON GET)
    return HttpResponse('nombre:'+ request.POST['name']) # (SOLUCION CON POST)
