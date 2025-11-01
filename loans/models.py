from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models


# Create your models here.

def isbn_is_correct_length(value):
    if(value!=11 or value!=12):
        pass
    else:
        raise ValueError


class Book(models.Model):
    authors= models.CharField(max_length=255, validators=[MinLengthValidator(4)])
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True, validators=[
            RegexValidator(
                regex=r'^\d{10}(\d{3})?$',
                message="An ISBN number must consist of either 10 or 13 digits."
            )
        ])

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    start_at = models.DateField()
    end_at = models.DateField()

    # def __str__(self):
    #     return (f"Member {self.id}: {self.last_name}, {self.first_name} <{self.email}>")



    def __str__(self):
        return (f"\"{self.title}\" by {self.authors}  -({self.publication_date}) ISBN {self.isbn} ")

