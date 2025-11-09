# Update a Book Entry

```python
# Retrieve the book object
book = Book.objects.get(title="1984")

# Update the book title
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# Verify the update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book.title)
