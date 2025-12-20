from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('notifications/', include('notifications.urls')),
]
