from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Book, Genre
from .forms import SignupForm, LoginForm
import random
from random import shuffle
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Automatically log the user in
            return redirect('home')  # Redirect to the home page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect if the user is already logged in

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

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
    widths = ["w-3/4", "w-10/12", "w-4/5", "w-5/6", "w-9/12"]

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