from django.test import TestCase
from django.urls import reverse

from .models import Publisher, Book


class BookListTest(TestCase):

    def test_book_appears_on_books_page(self):
        publisher = Publisher.objects.create(
            name="Test Publisher"
        )

        Book.objects.create(
            title="Unique Testing Book",
            page_count=250,
            publisher=publisher
        )

        response = self.client.get(
            reverse("book_list")
        )

        self.assertContains(
            response,
            "Unique Testing Book"
        )