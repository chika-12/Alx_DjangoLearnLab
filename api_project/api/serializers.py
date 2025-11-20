from rest_framework import serializers
from . import models

class BookSerializer(serializers.ModelSerializer):
  class Mete:
    model = models.Book
    fields = "__all__"
    