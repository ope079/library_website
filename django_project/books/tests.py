from django.test import TestCase
from django.urls import reverse

from .models import Book
# Create your tests here.

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Book Title",
            subtitle = "Book Sub Title",
            author = "Author",
            isbn = "1234567891012",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Book Title")
        self.assertEqual(self.book.subtitle, "Book Sub Title")
        self.assertEqual(self.book.author, "Author")
        self.assertEqual(self.book.isbn, "1234567891012")
        self.assertEqual(Book.objects.count(), 1)

    def test_book_list(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sub Title")
        self.assertTemplateUsed(response, 'books/book_list.html')