from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import Book

class BookViewTest(APITestCase):

    def test_response_is_correct(self):
        book = Book.objects.create(
            title='Test Book', 
            author='Author Name',
            description='A test book description.'
            )

        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == 200
        first_book = response.data[0]
        assert first_book['title'] == book.title
        assert first_book['author'] == book.author
        assert first_book['description'] == book.description
      