from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views  # for auth views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Blog app
    path('', include('blog.urls')),

    # Auth routes
    path('register/', blog_views.register_view, name='register'),
    path('login/', blog_views.login_view, name='login'),
    path('logout/', blog_views.logout_view, name='logout'),
    path('profile/', blog_views.profile_view, name='profile'),
]
