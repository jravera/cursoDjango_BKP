from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date


def create(request):
    rep = Reporter(firstName='juanjo',lastName='perez', eMail='juanjo@demo.com')
    rep.save()

    art1 = Article(headline='headline articulo 1', pubDate=date(2024,12,24), reporter=rep )
    art2 = Article(headline='headline articulo 2', pubDate=date(2024,7,15), reporter=rep )
    art3 = Article(headline='headline articulo 3', pubDate=date(2023,11,25), reporter=rep )

    art1.save()
    art2.save()
    art3.save()

    # Consulto el reportero desde el articulo
    #result = art1.reporter.firstName

    # Consulto los articulos desde el reportero
    result = rep.article_set.all()  # Aca el return es: return HttpResponse( result )

    return HttpResponse( result )

