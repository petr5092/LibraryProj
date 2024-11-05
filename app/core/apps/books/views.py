from typing import Any
from django.db.models.query import QuerySet
from core.apps.books.models import (
    Book,
    Library,
)
from core.apps.books.forms import (
    BookCreateForm,
    LibraryCreateForm,
)
from django.urls import reverse, reverse_lazy
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from core.apps.books.serializer import BookSerializers, LibrarySerializers
from rest_framework import status
from rest_framework.views import APIView


class BookListView(ListAPIView):
    model = Book
    template_name = "books/head.html"
    context_object_name = "books"
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    
    def get_queryset(self) -> QuerySet[Any]:
        return (
            super()
            .get_queryset()
            .select_related("library")
            .all()
        )
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class GetBook(RetrieveAPIView):
    model = Book
    template_name = "books/book.html"
    context_object_name = "book"
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = "pk"

    
    def get_queryset(self) -> QuerySet[Any]:
        return (
            super()
            .get_queryset()
            .select_related("library")
            .all()
        )

class FilterLib(BookListView):
    def get_queryset(self) -> QuerySet[Book]:
        return (
            super()
            .get_queryset()
            .filter(library_id=self.kwargs["lib_id"])
            .select_related("library")
            .all()
        )


class AddBook(CreateAPIView):
    model = Book
    form_class = BookCreateForm
    template_name = "books/create_book.html"
    serializer_class = BookSerializers

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("add_book")
    

class AddLib(CreateAPIView):
    model = Library
    form_class = LibraryCreateForm
    template_name = "books/create_lib.html"
    serializer_class = LibrarySerializers

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("add_lib")


class UpdateBook(UpdateAPIView):
    model = Book
    fields = ["description", "library"]
    template_name = 'books/update_book.html'
    context_object_name = "book"
    pk_url_kwarg = "book_id"
    success_url = reverse_lazy("main")
    serializer_class = BookSerializers


class UpdateLib(UpdateAPIView):
    model = Library
    fields = ["description"]
    template_name = 'books/update_lib.html'
    context_object_name = "lib"
    pk_url_kwarg = "lib_id"
    success_url = reverse_lazy("main")
    

class DeleteBook(APIView):
    def delete(self, request, book_id):
        obj = Book.objects.get(pk=book_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteLib(APIView):
    def delete(self, request, lib_id):
        obj = Library.objects.get(pk=lib_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
