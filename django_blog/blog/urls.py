from django.urls import path
from . import views

urlpatterns = [
    # ---- Post URLs ----
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # ---- Comment URLs ----
    path('post/<int:post_id>/comment/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # ---- Auth URLs ----
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # ---- Search & Tags ----
    path('search/', views.search_posts, name='search-posts'),
    path('tag/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'),
]
