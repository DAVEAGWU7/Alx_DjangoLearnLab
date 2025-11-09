from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),

    # Library and book views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role-based URLs
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
