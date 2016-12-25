from rest_framework import serializers
from eae.models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('pk', 'first_name', 'last_name', 'display_name')


class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ('pk', 'tittle', 'books')


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ('pk', 'tittle', 'authors', 'desc')