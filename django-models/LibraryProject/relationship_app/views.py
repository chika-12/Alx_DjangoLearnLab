from django.shortcuts import render, redirect

# Create your views here.
from .models import Author, Librarian, Book
from .models import Library
from django.http import JsonResponse
from django.views.generic.detail import DetailView

code = "relationship_app/list_books.html"
code = "relationship_app/library_detail.html"

def list_books(request):
  if request.method == "GET":
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)

def add_books(request):
  if request.method == "POST":

    title = request.POST.get('title')
    author_name = request.POST.get('author')
    author, created = Author.objects.get_or_create(name=author_name)

    Book.objects.create(title=title, author=author)
    return redirect('list_books')
  return render(request, "add_book.html")

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['books'] = self.object.books.all()
    return context


