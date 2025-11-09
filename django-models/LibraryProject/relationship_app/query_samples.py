from relationship_app.models import Author, Book, Library, Librarian

# Create some authors
author1 = Author.objects.create(name="George Orwell")
author2 = Author.objects.create(name="J.K. Rowling")

# Create some books
book1 = Book.objects.create(title="1984", author=author1)
book2 = Book.objects.create(title="Harry Potter", author=author2)

# Create a library and add books
library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)

# Create a librarian
librarian = Librarian.objects.create(name="Alice", library=library)

# Queries
# 1. All books by George Orwell
books_by_orwell = Book.objects.filter(author__name="George Orwell")
print(books_by_orwell)

# 2. All books in Central Library
all_books_in_library = library.books.all()
print(all_books_in_library)

# 3. Retrieve the librarian of Central Library
print(library.librarian)
