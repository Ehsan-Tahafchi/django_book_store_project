from django.shortcuts import render
from django.views import generic
from books.models import Book
from django.views.generic.base import TemplateView


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'
