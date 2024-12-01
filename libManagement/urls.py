from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("books/", views.books, name="books"),
    path('book/<int:id>/', views.book, name='book-detail'),
]