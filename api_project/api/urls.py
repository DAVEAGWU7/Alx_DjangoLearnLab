from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDeleteView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
]


from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
