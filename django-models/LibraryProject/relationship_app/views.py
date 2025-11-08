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
from django.contrib.auth.models import User
#from .utils import is_admin, is_librarian, is_member
from django.contrib.auth.decorators import user_passes_test
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


def is_admin(user):
  return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

def is_librarian(user):
  return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

def is_member(user):
  return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'member'


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



# class CustomLoginView(LoginView):
#   template_name = 'login.html'
#   redirect_authenticated_user = True
#   success_url = reverse_lazy('list_books')

# class CustomLogoutView(LogoutView):

#   template_name = 'logout.html'
