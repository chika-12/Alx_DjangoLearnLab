## To update a book 
b1 = Book.objects.get(id=1)
b1.title = "Nineteen Eighty-Four"
b1.save()
