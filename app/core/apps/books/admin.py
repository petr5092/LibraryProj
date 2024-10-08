from django.contrib import admin

from core.apps.books.models import Book, Library

@admin.register(Book, Library)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk',)
