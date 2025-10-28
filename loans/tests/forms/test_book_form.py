from datetime import datetime

from django.test import TestCase
from loans.forms import BookForm
from loans.models import Book
from django import forms

class BookFormTestCase(TestCase):
    def test_form_has_necessary_fields(self):
        form = BookForm()
        self.assertIn('authors', form.fields)
        self.assertIn('title', form.fields)
        self.assertIn('publication_date', form.fields)
        self.assertIn('isbn', form.fields)

    def test_form_author_is_minimum_length(self):
        form_data = {'authors': 'A',  # too short
            'title': 'A title',
            'publication_date': datetime(2022, 9, 1),
            'isbn': '1234567890123'}
        form = BookForm(form_data)
        self.assertFalse(form.is_valid())
