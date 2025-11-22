from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ListAPIView for simple listing
class BookList(generics.ListAPIView):
    """
    Endpoint to list all books (no authentication required for listing).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet with full CRUD and authentication
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for the Book model.
    Authentication required: only authenticated users can create, update, or delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
