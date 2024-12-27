from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Article, Publications


def create(request):
    # ----------------------------------------------------------------
    # Todo este comentado corresponde al acceso a la relacion por
    # "articulo" que es donde anclamos en el codigo la relacion N a N
    # ----------------------------------------------------------------
    # art1 = Article(headline = 'Articulo 1')
    # art1.save()
    # art2 = Article(headline = 'Articulo 2')
    # art2.save()
    # art3 = Article(headline = 'Articulo 3')
    # art3.save()
    # El .save() siempre debe ser previo a la generacion de la vista N a N

    # pub1 = Publications(title = 'Publicacion 1')
    # pub1.save()
    # pub2 = Publications(title = 'Publicacion 2')
    # pub2.save()
    # pub3 = Publications(title = 'Publicacion 3')
    # pub3.save()
    # pub4 = Publications(title = 'Publicacion 4')
    # pub4.save()
    # pub5 = Publications(title = 'Publicacion 5')
    # pub5.save()
    # pub6 = Publications(title = 'Publicacion 6')
    # pub6.save()
    # pub7 = Publications(title = 'Publicacion 7')
    # pub7.save()
    # El .save() siempre debe ser previo a la generacion de la vista N a N

    # Armo las relaciones
    # art1.publications.add(pub1)
    # art1.publications.add(pub2)
    # art1.publications.add(pub3)
    # art2.publications.add(pub4)
    # art2.publications.add(pub5)
    # art2.publications.add(pub6)
    # art3.publications.add(pub7)
    # art3.publications.add(pub2)
    # art3.publications.add(pub5)

    # La relacion N a N esta en la clase Article

    # ----------------------------------------------------------------
    #
    # Fin del comentario
    # 
    # ----------------------------------------------------------------

    # Si quiero eliminar una relacion lo que hago es
    #art1.publications.remove(pub1)

    # Un articulo esta en muchas publicaciones
    # ----------------------------------------
    # art1 = Article.objects.get(id = 1)
    # result = art1.publications.all()

    # return HttpResponse(result)

    # Una publicacion contiene muchos articulos
    # -----------------------------------------
    pub2 = Publications.objects.get(id = 2)
    result = pub2.article_set.all()
 
 
    return HttpResponse(result)

