```markdown
# Delete a Book Entry

```python
# Retrieve the book object by its title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book from the database
book.delete()

# Verify deletion (this will raise an error if the book no longer exists)
try:
    Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Book successfully deleted.")