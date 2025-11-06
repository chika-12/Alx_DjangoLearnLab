from .models import Book, Librarian, Library, Auhor

def filter_by_author(author):
  books_by_author = Book.objects.filter(author=author)
  return books_by_author

def all_books():
  books = Book.objects.get()
  return books

def retrive_librarian(library):
  librarian = Librarian.objects.filter(library=library)
  return librarian
  