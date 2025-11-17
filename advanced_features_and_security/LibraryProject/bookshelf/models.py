from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
  def create_user(self, username, email, password=None, **extra_fields):
    if not email:
      raise ValueError("Email is required")
    
    email = self.normalize_email(email)
    user = self.model(username=username, email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, username, email, password=None, **extra_fields):
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_staff', True)

    if extra_fields.get('is_superuser') is False:
      raise ValueError('Superuser must have is_superuser=True')
    if extra_fields.get('is_staff') is False:
      raise ValueError("Superuser must have is_staff=True")
    return self.create_user(username=username, email=email, password=password, **extra_fields)


class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)
  date_of_birth = models.DateTimeField(null=True, blank=True)
  profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

  USERNAME_FIELD = 'email'  # use email to login
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # username is still required when creating superusers

  
  objects = CustomUserManager()
  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  
class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField()
  

  #can_view, can_create, can_edit, and can_delete 

  class Meta:
    permissions = [
      ("can_view", "Can view"),
      ("can_create", "Can create"),
      ("can_edit", "Can edit"),
      ("can_delete", "Can delete")
    ]

  def __str__(self):
    return f"{self.title} was written by {self.author} in {self.publication_year}"
  

