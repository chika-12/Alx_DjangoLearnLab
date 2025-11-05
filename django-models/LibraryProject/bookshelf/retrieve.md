## To retrieve all books in db
Book.objects.all()

## To retrive by id 
b1 = Book.objects.get(publication_year=1984)
print(b1)
