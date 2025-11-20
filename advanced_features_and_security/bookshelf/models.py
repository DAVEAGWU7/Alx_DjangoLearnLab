from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published = models.DateField()

    class Meta:
        permissions = [
            ("can_view", "Can view book records"),
            ("can_create", "Can create book records"),
            ("can_edit", "Can edit book records"),
            ("can_delete", "Can delete book records"),
        ]

    def __str__(self):
        return self.title
