from django.test import TestCase
from django.urls import reverse

class CreateBookTestCase(TestCase):
    def setUp(self):
        self.url = reverse('create-book')

    def test_create_book_url(self):
        self.assertEqual(self.url, "/create_book/")