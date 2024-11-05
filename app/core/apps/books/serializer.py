from rest_framework import serializers

from core.apps.books.models import Book, Library


class BookSerializers(serializers.ModelSerializer):


    class Meta:
        model = Book
        fields = "__all__"


class LibrarySerializers(serializers.ModelSerializer):


    class Meta:
        model = Library
        fields = "__all__"


