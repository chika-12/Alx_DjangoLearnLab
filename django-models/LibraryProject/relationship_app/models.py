from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=200)

class Book(models.Model):
  title = models.CharField(max_length=200) 
  author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Library(models.Model):
  name = models.CharField(max_length=200)
  books = models.ManyToManyField('Book')

  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=200)
  library = models.OneToOneField('Library', on_delete=models.CASCADE)

class UserProfile(models.Model):

  ROLE_CHOICE = [
    ("admin", "Admin"),
    ("librarians", "Librarians"),
    ('member', "Member")
  ]
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(choices=ROLE_CHOICE, default='member')