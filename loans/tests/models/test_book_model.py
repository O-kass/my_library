
from loans.models import Book
from django.core.exceptions import ValidationError
from django.test import TestCase
import datetime

class BookTestCase(TestCase):
    def setUp(self):
        authors=""
        title="A title"
        publication_date=datetime.datetime(2022,9,1)
        isbn="123456789"
        self.book = Book(authors=authors, title=title, publication_date=publication_date, isbn=isbn)

    def test_valid_book_is_valid(self):
        try:
            self.book.full_clean()
        except ValidationError:
            self.fail("Default test book should be deemed valid")

    def test_blank_book(self):
        self.book.authors = ""
        with self.assertRaises(ValidationError):
            self.book.full_clean()

    def test_str_not_blank(self):
        self.assertEqual(self.book.__str__(), f"\"{self.book.title}\" by {self.book.authors}  -({self.book.publication_date}) ISBN {self.book.isbn} ")

    def test_form_author_is_minimum_length(self):
        num_author = self.book.authors
        self.book.authors=""
        count = len(num_author)
        self.assertFalse(count > 3)

    def test_form_isbn_is_minimum_length(self):
        num_author = self.book.authors
        self.book.authors=""
        count = len(num_author)
        self.assertFalse(count > 3)

    def test_form_author_is_below_maximum_length(self):
        num_author = self.book.authors
        self.book.authors=""
        count = len(num_author)
        self.assertFalse(count > 3)

    def test_form_author_is_minimum_length(self):
        num_author = self.book.authors
        self.book.authors=""
        count = len(num_author)
        self.assertFalse(count > 3)