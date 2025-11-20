from django.urls import path
from .views import BookList, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("allList/", BookViewSet, basename='allList')

urlpatterns = [
  path("list/", BookList.as_view(), name='book_list'),
] + router.urls