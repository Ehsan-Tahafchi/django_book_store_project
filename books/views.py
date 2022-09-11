from django.views import generic
from .models import Book
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comment = book.comments.all()

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
    return render(request, 'books/book_detail.html', {'book': book, 'comment': comment, 'comment_form': comment_form})


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('BookListView')
