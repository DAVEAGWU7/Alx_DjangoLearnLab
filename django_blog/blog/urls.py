from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    # Post URLs
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post-list"),
    path("post/<int:pk>/", views.post_detail, name="post-detail"),
    path("post/new/", views.post_create, name="post-create"),
    path("post/<int:pk>/update/", views.post_update, name="post-update"),
    path("post/<int:pk>/delete/", views.post_delete, name="post-delete"),

    # 🔥 Required by your ALX task
    path("post/<int:pk>/comments/new/", views.comment_create, name="comment-create"),
    path("comment/<int:pk>/update/", views.comment_update, name="comment-update"),
    path("comment/<int:pk>/delete/", views.comment_delete, name="comment-delete"),
]
