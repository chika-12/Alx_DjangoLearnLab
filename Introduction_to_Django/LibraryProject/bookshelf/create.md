## The following code creates a book and save to database
b1 = Book(title="1984", author="George Orwell", publication_year=1949)
b1.save()

## Alternatively
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)