from django.contrib import admin
from django.urls import path, include
from core.apps.books.views import BookListView, GetBook, FilterLib, AddBook, AddLib, UpdateBook, UpdateLib, DeleteBook, DeleteBook
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', BookListView.as_view(), name='main'),
    path('books/<int:pk>/', GetBook.as_view()),
    path('lib/<int:lib_id>/', FilterLib.as_view()),
    path('create_book/', AddBook.as_view(), name='add_book'),
    path('create_lib/', AddLib.as_view(), name='add_lib'),
    path('update_book/<int:book_id>/', UpdateBook.as_view(), name='update_book'),
    path('update_lib/<int:lib_id>/', UpdateLib.as_view(), name='update_lib'),
    path('del_book/<int:book_id>/', DeleteBook.as_view()),
    path('del_lib/<int:lib_id>/', DeleteBook.as_view()),
] + debug_toolbar_urls()