from django.db import models

class Reporter(models.Model):
    firstName = models.CharField(max_length=50, default='')
    lastName  = models.CharField(max_length=50, default='')
    eMail     = models.EmailField()

    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField( max_length=100)
    pubDate  = models.DateField( auto_now=True, auto_now_add=False)
    reporter = models.ForeignKey(Reporter, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.headline