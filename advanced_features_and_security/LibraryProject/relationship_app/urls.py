from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books

code = "views.register"
urlpatterns = [
  path("books/", views.list_books, name='list_books'),
  path("books/add/", views.add_books, name="add_books"),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
  path("users/", views.show_user, name="users"),
  path("admin/", views.admin_dashboard, name="admin_dashboard"),
  path("librarian/", views.librarian_dashboard, name='librarian_dashboard'),
  path("member/", views.member_dashboard, name="member_dashboard"),

  #Authentication
  path('register/', views.register, name="register"),
  path('login/', views.RoleBaseLogin.as_view(template_name='login.html'), name="login"),
  path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout")
]