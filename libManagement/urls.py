from django.urls import path
from . import views

from .views import signup_view, login_view, delete_book, update_book_status, logout_view, borrow_book

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("books/", views.books, name="books"),
    path('book/<int:id>/', views.book, name='book-detail'),
    path('register/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path("lib-admin/", views.librarian, name="librarian"),
    path("delete-book/<int:id>/", delete_book, name="delete_book"),
    path('update-book-status/<int:book_id>/', views.update_book_status, name='update_book_status'),
    path('logout/', logout_view, name='logout'),
    path('borrow/<int:bookId>/', borrow_book, name='borrow_book'),
]