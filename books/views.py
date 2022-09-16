from django.views import generic
from .models import Book
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import SearchForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    is_favourite = False
    comment = book.comments.all()

    if book.favourite.filter(pk=request.user.id).exists():
        is_favourite = True

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'books/book_detail.html',
                  {'book': book, 'comment': comment, 'comment_form': comment_form, 'is_favourite': is_favourite})


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_create.html'


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('BookListView')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


def book_search(request):
    books = Book.objects.all()
    form = SearchForm()
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data['search']
            books = Book.objects.filter(title__icontains=cd)
    return render(request, 'books/book_search.html', {'books': books, 'form': form})


def favourite_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.favourite.filter(pk=request.user.id).exists():
        book.favourite.remove(request.user)
    else:
        book.favourite.add(request.user)

    return HttpResponseRedirect(book.get_absolute_url())


def book_favourite_list(request):
    user = request.user
    favourite_books = user.favourite.all()
    return render(request, 'books/book_favourite_list.html', {'favourite_books': favourite_books})
