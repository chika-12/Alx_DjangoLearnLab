## To retrieve all books in db
Book.objects.all()

## To retrive by id 
b1 = Book.objects.get(id=1)
print(b1)