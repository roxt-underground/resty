from django.contrib import admin

from books.models import Book, Author, Cover


@admin.register(Book, Author, Cover)
class Admin(admin.ModelAdmin):
    pass
