from django.urls import path
from . import views
from .views import signup_view, login_view 

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("books/", views.books, name="books"),
    path('book/<int:id>/', views.book, name='book-detail'),
    path('register/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
]