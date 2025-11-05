# delete.md

from bookshelf.models import Book

# Retrieve the book and delete it
book = Book.objects.get(title="1984")
book.delete()
