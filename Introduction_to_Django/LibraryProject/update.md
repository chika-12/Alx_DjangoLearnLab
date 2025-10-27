## To update a book 
b1 = Book.objects.get(id=1)
b1.title = "1984"
b1.save()
