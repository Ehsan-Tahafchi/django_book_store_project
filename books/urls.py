from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, book_detail_view, book_search, \
    favourite_book,book_favourite_list

urlpatterns = [
    path('', BookListView.as_view(), name='BookListView'),
    path('<int:pk>/', book_detail_view, name='BookDetailView'),
    path('new/', BookCreateView.as_view(), name='BookCreateView'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='BookUpdateView'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='BookDeleteView'),
    path('search/', book_search, name='book_search'),
    path('<int:pk>/favourite_book/', favourite_book, name='favourite_book'),
    path('favourite_list/', book_favourite_list, name='book_favourite_list'),



]
