from django.contrib import admin
from .models import Book

# Customize how the Book model appears in the admin panel
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in list view
    search_fields = ('title', 'author')                      # Add a search box
    list_filter = ('publication_year',)                      # Add filter sidebar

# Register the Book model with the custom admin settings
admin.site.register(Book, BookAdmin)
