from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from rest_framework.permissions import BasePermission
from django.contrib.contenttypes.models import ContentType
User = get_user_model()

user = User.objects.get(email='mark@gmail.com')
from .models import Book
book_ct = ContentType.objects.get_for_model(Book)
perm = Permission.objects.get(codename='can_create', content_type=book_ct)
user.user_permissions.add(perm)

# bookshelf/permissions.py

class CanCreateBookPermission(BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated and request.user.has_perm('bookshelf.can_create')
