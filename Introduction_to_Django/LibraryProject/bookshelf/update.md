# update.md

from bookshelf.models import Book

# Retrieve the book and update its publication year
book = Book.objects.get(title="1984")
book.publication_year = 1950
book.save()
