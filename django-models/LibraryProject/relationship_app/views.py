from django.shortcuts import render, redirect

# Create your views here.
from .models import Author, Librarian, Library, Book
from django.http import JsonResponse
from django.views.generic import DeleteView

code = "relationship_app/list_books.html"

def list_all_books(request):
  if request.method == "GET":
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "list_book.html", context)

def add_books(request):
  if request.method == "POST":

    title = request.POST.get('title')
    author_name = request.POST.get('author')
    author, created = Author.objects.get_or_create(name=author_name)

    Book.objects.create(title=title, author=author)
    return redirect('list_books')
  return render(request, "add_book.html")

class LibraryDetailView(DeleteView):
  model = Library
  template_name = 'library_detail.html'
  context_object_name = 'library'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['books'] = self.object.books.all()
    return context


