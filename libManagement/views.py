from django.shortcuts import render, HttpResponse
from .models import Book
import random
# Create your views here.

def home(request):
    books = Book.objects.all()
    def getBook():
        temp =0
        for book in books:
            
            list1 = [90,45]
            colors =[ "050506","2B154B","6F0731"]
            n = random.choice(list1)
            book.dbug = str(temp)
            if temp == 90:  
                if n == 45:
                    
                    book.style= "rotate-"+str(n) +" -ml-3 -mr-12 mb-3 mt-3"
                else:
                    
                    book.style= "rotate-"+str(n)+" -mx-12"
            elif temp == 0:
                if n == 45:
                    book.style= "rotate-"+str(n) +" -ml-7 -mr-12 -mb-1 mt-3"
                else:
                    book.style= "rotate-"+str(n) +" -mx-12 "
            else:
                if n == 45:
                    
                    book.style= "rotate-"+str(n)+" -ml-9 -mr-12 -mb-2 mt-3"
                else:
                    
                    book.style= "rotate-"+str(n)+" -ml-3 -mr-12 "
                
            book.color= "bg-[#"+random.choice(colors)+"]"
            temp = n
       
    getBook()
    return render(request, "home.html", {"books": books})

def books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})

def book(request):
    books = Book.objects.all()
    return render(request, "book.html", {"books": books})