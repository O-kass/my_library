from loans import models
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Help text goes here"

    def handle(self, *args, **options):
        models.Book.objects.all().delete()