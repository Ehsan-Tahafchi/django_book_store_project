from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='BookListView'),
    path('<int:pk>/', BookDetailView.as_view(), name='BookDetailView'),
    path('new/', BookCreateView.as_view(), name='BookCreateView'),

]
