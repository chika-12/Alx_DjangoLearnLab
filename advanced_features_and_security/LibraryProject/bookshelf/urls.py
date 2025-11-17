from django.urls import path
from . import views
urlpatterns = [
  path('getAllUsers/', views.getAllUsers, name="users"),
  path('login/', views.login, name="login"),
  path('booklist/', views.book_list, name="booklist")
]