from rest_framework import serializers
from . models import Book, Autor

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'