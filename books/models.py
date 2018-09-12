from django.db import models


class Book(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=600, null=True, blank=True)
    authors = models.ManyToManyField('Author', related_name='books')


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)


class Cover(models.Model):
    cover = models.ImageField()
    book = models.OneToOneField('Book', related_name='cover', null=True, blank=True, on_delete=models.SET_NULL)
