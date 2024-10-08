from typing import Any
from django.db.models.query import QuerySet
from django.contrib.auth.models import User, AnonymousUser
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from core.apps.books.models import (
    Book,
    Library,
)
from core.apps.books.forms import (
    BookCreateForm,
    LibraryCreateForm,
)
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, TemplateView


class BookListView(ListView):
    model = Book
    template_name = "books/head.html"
    context_object_name = "books"
    
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


class GetBook(DetailView):
    model = Book
    template_name = "books/book.html"
    context_object_name = "book"
    pk_url_kwarg = "book_id"


class FilterLib(BookListView):
    def get_queryset(self) -> QuerySet[Book]:
        return (
            super()
            .get_queryset()
            .filter(library_id=self.kwargs["lib_id"])
            .select_related("library")
            .all()
        )


class AddBook(CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = "books/create_book.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("add_book")
    

class AddLib(CreateView):
    model = Book
    form_class = LibraryCreateForm
    template_name = "books/create_lib.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("add_lib")


def get_file(request, book_id):
    book = Book.objects.get(pk=book_id)
    response = HttpResponse(book.doc, content_type="app/core/media")
    print(book.doc)
    response['Content-Disposition'] = f'attachment; filename="{book.doc.name}"'
    return response


def del_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def del_lib(request, lib_id):
    lib = Library.objects.get(pk=lib_id)
    lib.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])