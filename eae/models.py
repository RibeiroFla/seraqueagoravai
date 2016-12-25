from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return u'{l}, {f}'.format(l=self.last_name, f=self.first_name)


class Book(models.Model):
    tittle = models.CharField(max_length=100)
    desc = models.TextField(max_length=100, blank=True)
    authors = models.ManyToManyField(Author, blank=True)

    def __unicode__(self):
        return self.tittle


class Shelf(models.Model):
    tittle = models.CharField(max_length=100)
    books = models.ManyToManyField(Book,blank=True)

    def __unicode__(self):
        return self.tittle