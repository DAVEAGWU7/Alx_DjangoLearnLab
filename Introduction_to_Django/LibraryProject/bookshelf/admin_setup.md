# Django Admin Integration for Book Model

## Steps Implemented

1. Registered the `Book` model in `bookshelf/admin.py`.
2. Created a custom `BookAdmin` class to improve the admin interface.
3. Added `list_display`, `search_fields`, and `list_filter` for better usability.
4. Created a superuser to access the Django admin dashboard.
5. Verified successful Book management through the admin interface.

---

## Code Used (bookshelf/admin.py)

```python
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)
