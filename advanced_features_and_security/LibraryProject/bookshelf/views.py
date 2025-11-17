from django.shortcuts import render
from . import models
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import permission_required

# Create your views here.
@api_view(["POST"])
def login(request):
  email = request.data.get("email")
  password = request.data.get("password")

  if not email or not password:
    return Response({"Email and password required"})
  
  try:
    user = models.CustomUser.objects.get(email=email)
    if user.check_password(password):
      token, create = Token.objects.get_or_create(user=user)
      return Response({
      "message": "Login successful",
      "token": token.key,
      "user": {
        "id": user.id,
        "email": user.email,
        "username": user.username
        }
    })

  except models.CustomUser.DoesNotExist:
    return Response({"Invalid credentials"})
   

@api_view(["GET"])
@permission_required('bookshelf.can_create')
def getAllUsers(request):
  
  user = models.CustomUser.objects.all()
  serialize = serializers.UserSerilizers(user, many=True)
  return Response({
    "message": "successful",
    "data": serialize.data
  })
