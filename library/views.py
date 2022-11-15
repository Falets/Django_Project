from django.shortcuts import render
from library.models import Book, Genre, Post, BookIns
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from library.forms import ChangeBookForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
import datetime
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy



def home(request):
	num_books = Book.objects.all().count()
	num_instances = BookIns.objects.all().count()
	num_instances_available = BookIns.objects.filter(status__exact='a').count()
	num_genres = Genre.objects.all().count()
	context = {
		"num_books": num_books,
		"num_instances": num_instances,
		"num_instances_available": num_instances_available,
		"num_genres": num_genres
	}
	return render(request, 'library/index.html', context)

def about(request):
	context = {
		'title': 'About page'
	}
	return render(request, 'library/about.html', context)

class BookListView(ListView):
	model = Book
	template_name = "library/books.html"
	context_object_name = "books"
	paginate_by = 2

class BookDetailView(DetailView):
	model = Book
	template_name = "library/book-detail.html"

class RentedBooksByUserListView(LoginRequiredMixin, ListView):
	model = BookIns
	template_name ="library/bookinstance_list_renter_user.html"
	context_object_name = "books"
	paginate_by = 10

	def get_queryset(self):
		return BookIns.objects.filter(renter=self.request.user).filter(status__exact='o').order_by('due_back')

class BookUpdate(PermissionRequiredMixin, UpdateView):
	permission_required = 'library.can_ever'
	model = BookIns
	fields = ['renter', 'due_back', 'status']
	success_url = reverse_lazy('libbooks')
	template_name = 'library/book_renew_librarian.html'