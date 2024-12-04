from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models import Q
from django.contrib.auth.hashers import make_password
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Book(models.Model):
    bookId = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100, default="Unknown")
    year_published = models.IntegerField(null=True, blank=True, default=0)
    edition = models.CharField(max_length=50, blank=True)
    synopsis = models.TextField(blank=True)
    status = models.CharField(max_length=50, default="Unknown")  
    book_type = models.CharField(max_length=50, default="Unknown")  
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True, related_name="books")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class UserManager(BaseUserManager):
    
    def create_user(self, username, password, first_name, last_name, user_type, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, first_name=first_name, last_name=last_name, user_type=user_type, **extra_fields)
        user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, first_name, last_name, user_type, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, first_name, last_name, user_type, **extra_fields)
    
    
class User(AbstractBaseUser, PermissionsMixin):
    
    id = models.AutoField(primary_key=True) 
    username = models.CharField(max_length=100, unique=True, default=make_password('defaultpassword123'))
    password = models.CharField(max_length=100, default=make_password('defaultpassword123'))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('librarian', 'Librarian'),
    ])  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin access

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_type']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

class Borrow(models.Model):
    borrowId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrowed_books")
    borrow_date = models.DateField(auto_now_add=True)
    borrow_returned = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default="Borrowed")   

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'user'],
                condition=Q(borrow_returned__isnull=True),
                name='unique_active_borrow_per_user'
            )
        ]

    def __str__(self):
        return f"{self.user} borrowed {self.book} on {self.borrow_date}"