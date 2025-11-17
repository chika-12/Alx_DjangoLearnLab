from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
User = get_user_model()

user = User.objects.get(email='mark@gmail.com')
perm = Permission.objects.get(codename='can_create')
user.user_permissions.add(perm)