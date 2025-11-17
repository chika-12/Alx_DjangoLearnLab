from rest_framework import serializers
from . import models

class UserSerilizers(serializers.ModelSerializer):
  class Meta:
    model = models.CustomUser
    fields = "__all__"

class BookSerialiazer(serializers.ModelSerializer):
  class Meta:
    model = models.Book
    fields = "__all__"