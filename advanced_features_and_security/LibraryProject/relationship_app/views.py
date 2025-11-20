from django.shortcuts import render, redirect

# Create your views here.
from .models import Author, Librarian, Book
from .models import Library
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from .utils import is_admin, is_librarian, is_member
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
User = get_user_model()
# now use User.objects...

code = "relationship_app/list_books.html"
code = "relationship_app/library_detail.html"

def list_books(request):
  if request.method == "GET":
    books = Book.objects.all()
    context = {"books": books}
    template = loader.get_template('list_book.html')
    return HttpResponse(template.render(context, request))
    

def add_books(request):
  if request.method == "POST":

    title = request.POST.get('title')
    author_name = request.POST.get('author')
    author, created = Author.objects.get_or_create(name=author_name)

    Book.objects.create(title=title, author=author)
    return redirect('list_books')
  template = loader.get_template("add_book.html")
  return HttpResponse(template.render({}, request))

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'library_detail.html'
  context_object_name = 'library'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['books'] = self.object.books.all()
    return context

def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('list_books')
  else:
    form = UserCreationForm()
  return render(request, "register.html", {'form': form})

def show_user(request):
  user = User.objects.all()
  return render(request, "users.html", {"users": user})

@user_passes_test(is_admin, login_url='/login/')
def admin_dashboard(request):
  return render(request, 'admin_view.html')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_dashboard(request):
  return render(request, "librarian_view.html")

@user_passes_test(is_member, login_url='/login/')
def member_dashboard(request):
  return render(request, "member_view.html")


class RoleBaseLogin(LoginView):
  template_name = 'login.html'

  def get_success_url(self):
    user = self.request.user

    if hasattr(user, 'userprofile'):
      role = user.userprofile.role
      if role == 'admin':
        return '/relationship_app/admin/'
      elif role == 'librarian':
        return '/relationship_app/librarian/'
      elif role == 'member':
        return '/relationship_app/member/'
    return 'rlationship_app/register/'
  

class CustomLogoutView(LogoutView):
  template_name = 'logout.html'
