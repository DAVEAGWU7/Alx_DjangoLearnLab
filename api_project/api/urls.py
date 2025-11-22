from django.urls import path
from .views import BookList  # import the correct view

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
