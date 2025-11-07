from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

code = "views.register"
urlpatterns = [
  path("books/", views.list_books, name='list_books'),
  path("books/add/", views.add_books, name="add_books"),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

  #Authentication
  path('register/', views.register, name="register"),
  path('login/', LoginView.as_view(template_name='login.html'), name="login"),
  path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout")
]