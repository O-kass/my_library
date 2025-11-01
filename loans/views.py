from random import Random

from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from loans import models
from loans.models import Book
from loans.forms import BookForm

# import seed
# import unseed

# Create your views here.

ITEMS_PER_PAGE = 25


slogans = ["Believe in your shelf.",
		   "Need a good read? We’ve got you covered.",
		   "Get a better read on the world.",
		   "Having fun is not hard when you have a library card"
		   ]

#setup books in books list
# seed.retrieve_books()


#remove books
# unseed.removeData()
# booksList = ("Default", "Default", (2025-10-10), 676767)

def welcome(request):
	rand = Random()
	context = {'slogan': rand.choice(slogans)}
	return render(request, 'welcome.html', context)

def book_with_id(request, book_id):
	try:
		book = Book.objects.get(id=book_id)
		context = {'book': book}
		return render(request, 'book_id_specific.html', context)
	except:
		raise Http404(f"Could not find book with primary key {book_id}")

def create_book(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			try:
				form.save()
			except:
				form.add_error(None, "For some reason this book cannot be added to the database")
			else:
				path = reverse('books')
				return HttpResponseRedirect(path)
	else:
		form = BookForm()
	return render(request, 'create_book.html', {'form': form})

def update_book(request, book_id):
	try:
		book = Book.objects.get(id=book_id)
	except:
		raise Http404(f"Could not find book with primary key {book_id}")

	if request.method == "POST":
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			try:
				form.save()
			except:
				form.add_error(None, "For some reason this book cannot be added to the database")
			else:
				path = reverse('books')
				return HttpResponseRedirect(path)
	else:
		form = BookForm(instance=book)
	return render(request, 'update_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
	try:
		book = Book.objects.get(id=book_id)
	except:
		raise Http404(f"Could not find book with primary key {book_id}")
	if request.method == "POST":
		try:
			book.delete()
		except:
			raise Http404(f"Could not find book with primary key {book_id}")
		else:
			path = reverse('books')
			return HttpResponseRedirect(path)

	return render(request, 'delete.html', {'book': book})

def books(request):
	book_list = Book.objects.all()
	paginator = Paginator(book_list, ITEMS_PER_PAGE)
	page_number = request.GET.get("page")
	page_object = paginator.get_page(page_number)
	context = {'page_object': page_object}
	return render(request, 'books.html', context)








