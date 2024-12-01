from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Book, Genre
import random
from random import shuffle
# Create your views here.

def home(request):
    books = list(Book.objects.all())
    shuffle(books)
    def getBook():
        temp =0
        for book in books:
            
            list1 = [90,45]
            colors =[ "050506","3b0764","4a044e","4c0519", "082f49","1e1b4b"]
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
    query = request.GET.get('q')
    genre_filter = request.GET.get('genre') 
    books = Book.objects.all()
    genres = Genre.objects.all()

    if query:
        books = books.filter(name__icontains=query)

    if genre_filter:
        books = books.filter(genre__name=genre_filter)

    context = {
        'books': books,
        'genres': genres,
        'query': query,
        'selected_genre': genre_filter,
    }

    colors = ["3b0764","4a044e","4c0519", "082f49","1e1b4b"]
    widths = ["w-1/4", "w-2/5", "w-4/12", "w-5/12", "w-2/6"]

    books_list = list(books)
    for book in books_list:
        book.color = "bg-[#" + random.choice(colors) + "]"
        book.width = random.choice(widths)

    # Debug the context
    print("Context being sent to template:", context)

    return render(request, "books.html", context)

def book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book.html", {"book": book})