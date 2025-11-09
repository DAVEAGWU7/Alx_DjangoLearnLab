
---

## 🗂️ `CRUD_operations.md`
This one combines **all four operations** neatly for your submission.
```markdown
# CRUD Operations Summary

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>
