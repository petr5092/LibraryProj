from django.db import models

class Library(models.Model):
    description = models.CharField(max_length=100, verbose_name="Адрес")

    class Meta:
        verbose_name = "Библиотека"
        verbose_name_plural = "Библиотеки"
        db_table = "Library"
    
    def __str__(self):
        return f"Библиотека: {self.description}"


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=10000, verbose_name="Описание")
    doc = models.FileField(max_length=100, verbose_name="Файл книги")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    library = models.ForeignKey(
        Library,
        related_name="books",
        verbose_name="Библиотека",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        db_table = "books"

    def __str__(self):
        return self.title