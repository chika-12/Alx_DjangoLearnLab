## To delete a book
book = Book.objects.get(id=1)
book.delete()