from django.contrib import admin
from django.urls import path, include
from core.apps.books.views import BookListView, GetBook, FilterLib, AddBook, AddLib, UpdateBook, UpdateLib, get_file, del_book, del_lib


urlpatterns = [
    path('', BookListView.as_view(), name='main'),
    path('books/<int:book_id>/', GetBook.as_view()),
    path('books/<int:book_id>/get_file/', get_file),
    path('lib/<int:lib_id>/', FilterLib.as_view()),
    path('create_book/', AddBook.as_view(), name='add_book'),
    path('create_lib/', AddLib.as_view(), name='add_lib'),
    path('update_book/<int:book_id>/', UpdateBook.as_view(), name='update_book'),
    path('update_lib/<int:lib_id>/', UpdateLib.as_view(), name='update_lib'),
    path('del_book/<int:book_id>/', del_book),
    path('del_lib/<int:lib_id>/', del_lib),
]