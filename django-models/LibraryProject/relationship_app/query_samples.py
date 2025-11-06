from .models import Book, Librarian, Library, Author

def filter_by_author(author):
  books_by_author = Book.objects.filter(author=author)
  return books_by_author

def all_books():
  books = Book.objects.all()
  return books

def retrive_librarian(library):
  librarian = Librarian.objects.filter(library=library)
  return librarian

def list_all_books_in_library(library_name):
  books = Library.objects.get(name=library_name)
  return books.all()

def get_author_name(author_name):
  author  = Author.objects.get(name=author_name)
  return author


  