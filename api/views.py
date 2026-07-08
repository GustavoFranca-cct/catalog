from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookView(APIView):
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

book_view = BookView.as_view()
