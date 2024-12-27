from django.db import models
from django.http import HttpRequest

class Publications(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publications)

    def __str__(self):
        return self.headline
