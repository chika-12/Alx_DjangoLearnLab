from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book

# Create your views here.
from rest_framework.generics import ListAPIView

class BookList(ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer()
