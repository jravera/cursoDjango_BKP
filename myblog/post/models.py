from django.db import models
from datetime import date

class Autor(models.Model):
    name  = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name
    
class Entry(models.Model):
    autor      = models.ForeignKey(Autor, on_delete=models.CASCADE)
    headLine   = models.CharField(max_length=255)
    bodyText   = models.TextField()
    publicDate = models.DateField(default=date.today)
    rating     = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.headLine
