from django.urls import path
from .views import list_books, add_books, LibraryDetailView

urlpatterns = [
  path("books/", list_books, name='list_books'),
  path("books/add/", add_books, name="add_books"),
  path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]