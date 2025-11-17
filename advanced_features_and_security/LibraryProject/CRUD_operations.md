AttributeError: type object 'Book' has no attribute 'ojects'. Did you mean: 'objects'?
>>> Book.objects.all()
<QuerySet [<Book: Things Fall Apart was written by Chinua Achebe in 1967>]>
>>> b1 = Book.objects.get(id=1)
>>> b1.title = "984"
>>> b1.author = "George Orwell"
>>> b1.save()
>>> Book.objects.all()
<QuerySet [<Book: 984 was written by George Orwell in 1967>]>
>>> b1 = Book.objects.get(id=1)
>>> b1.title = "1984"
>>> b1.save()
>>> Book.objects.all()
<QuerySet [<Book: 1984 was written by George Orwell in 1967>]>
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> exit()