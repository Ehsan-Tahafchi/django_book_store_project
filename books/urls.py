from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='BookListView'),
    path('<int:pk>/', BookDetailView.as_view(), name='BookDetailView'),

]
