from faker import Faker
from loans import models
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Help text goes here"

    def handle(self, *args, **options):
        fake = Faker()

        for i in range(100):
            author = fake.name()
            title = fake.text(max_nb_chars=15)
            publication_date = fake.date()
            isbn = fake.port_number()
            book = models.Book(authors=author, title=title, publication_date=publication_date, isbn=isbn)
            book.save()








