from django.db import models
from django.db.models import Q

# Create your models here.



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
    
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=50)  
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrows")
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