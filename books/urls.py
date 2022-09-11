from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, book_detail_view

urlpatterns = [
    path('', BookListView.as_view(), name='BookListView'),
    path('<int:pk>/', book_detail_view, name='BookDetailView'),
    path('new/', BookCreateView.as_view(), name='BookCreateView'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='BookUpdateView'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='BookDeleteView'),



]
