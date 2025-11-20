from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"books_all", BookViewSet, basename='allList')

urlpatterns = [
  path("list/", BookList.as_view(), name='book_list'),
  path("", include(router.urls))
]