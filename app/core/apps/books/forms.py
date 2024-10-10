from typing import Any
from django import forms
from core.apps.books.models import Book, Library

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "description", "doc", "library",)
        widgets = {
            "title":forms.TextInput(attrs=({"class": "form-control"})),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "doc": forms.FileInput(attrs=({"class": "form-control"})),
            "library": forms.Select(attrs=({"class": "form-control"})),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
    
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title == "":
            return self.add_error("title", "а-та-та")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description == "":
            return self.add_error("description", "а-та-та")
        return description

    def clean_library(self):
        library = self.cleaned_data.get("library")
        if not (library):
            return self.add_error("library", "а-та-та")
        return library

    def is_valid(self):
        errors = self.errors.as_data()
        for field in self.fields:
            if field not in errors:
                self.fields[field].widget.attrs.update(
                    {"class": "form-control is-valid"}
                )
            else:
                self.fields[field].widget.attrs.update(
                    {"class": "form-control is-invalid"}
                )
        return super().is_valid()


class LibraryCreateForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ("description",)
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description == "":
            return self.add_error("description", "а-та-та")
        return description
    
    def is_valid(self):
        errors = self.errors.as_data()
        for field in self.fields:
            if field not in errors:
                self.fields[field].widget.attrs.update(
                    {"class": "form-control is-valid"}
                )
            else:
                self.fields[field].widget.attrs.update(
                    {"class": "form-control is-invalid"}
                )
        return super().is_valid()