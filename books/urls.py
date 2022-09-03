from django.contrib import admin
from django.urls import path, include
from .views import BookListView


urlpatterns = [
    path('', BookListView.as_view(), name ='BookListView'),

]
