from django.contrib import admin

from core.apps.books.models import Book, Library

@admin.register(Book, Library)
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk',)
