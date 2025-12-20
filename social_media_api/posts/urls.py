from django.urls import path
from .views import (
    PostListCreateView,
    FeedView,
    LikePostView,
    UnlikePostView
)

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('feed/', FeedView.as_view()),
    path('<int:pk>/like/', LikePostView.as_view()),
    path('<int:pk>/unlike/', UnlikePostView.as_view()),
]
