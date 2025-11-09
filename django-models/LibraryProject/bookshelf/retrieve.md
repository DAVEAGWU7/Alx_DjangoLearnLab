# retrieve.md

from bookshelf.models import Book

# Retrieve the book titled "1984"
book = Book.objects.get(title="1984")
print(book)
