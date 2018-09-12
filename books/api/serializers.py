from rest_framework import serializers

from books.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'user', 'name', 'description', 'authors')


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, queryset=Book.objects, required=False)

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'books')
