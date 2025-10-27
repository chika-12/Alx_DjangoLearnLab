## To delete a book
b1 = Book.objects.get(id=1)
b1.delete()
s