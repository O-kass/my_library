from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from loans.models import Book

class CreateBookTestCase(TestCase):
    def setUp(self):
        self.book = Book(authors="Jonah, J", title="Masked Menace",publication_date = datetime(2022, 9, 1),
        isbn = "123456789" )
        self.url = reverse('delete-book/{self.book.id}', kwargs={'book-id': self.book.id})

    def check_in_correct_url(self):
        self.assertEqual(self.url, f"/delete_book/{self.book.id}")

    def delete_works(self):
        self.book.save()
        before_count = Book.objects.count()
        self.url = reverse('delete-book/{self.book.id}', kwargs={'book-id': self.book.id})
        after_count = Book.objects.count()
