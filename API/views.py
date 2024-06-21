from rest_framework import viewsets
from .models import Book,Autor
from .serializers import BookSerializers

class ViewSetBook(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers