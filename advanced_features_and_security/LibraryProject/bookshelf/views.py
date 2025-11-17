from django.shortcuts import render
from . import models
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from . import serializers
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import permission_required
from rest_framework.permissions import DjangoModelPermissions
from .permission import CanCreateBookPermission


# Create your views here.
@api_view(["POST"])
def login(request):
  email = request.data.get("email")
  password = request.data.get("password")

  if not email or not password:
    return Response({"Email and password required"})
  
  user = authenticate(request, email=email, password=password)
  if user:
    token = RefreshToken.for_user(user)
    serialize = serializers.UserSerilizers(user)
    return Response({
      "message": "Login successful",
      "user": serialize.data,
      "access_token": str(token.access_token),
      "refresh_token": str(token),
    })
  else:
    return Response({"message": "Invalid Request"})
  


@api_view(["GET"])
@permission_classes([CanCreateBookPermission])
def getAllUsers(request):
  #user = request.user
  user = models.CustomUser.objects.all()
  serialize = serializers.UserSerilizers(user, many=True)
  return Response({
    "message": "successful",
    "data": serialize.data
  })

@permission_required('bookshelf.can_create', raise_exception=True)
@api_view(["GET"])
def book_list(request):
  book = models.Book.objects.all()
  serialize = serializers.BookSerialiazer(book, many=True)
  return Response({"message": "successful", "data": serialize.data})