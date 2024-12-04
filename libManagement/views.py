from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import JsonResponse 
from .models import Book, Genre, User, Borrow
from .forms import SignupForm, LoginForm
import random
from random import shuffle
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import json
import traceback

def logout_view(request):
    logout(request)
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('home') 
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) 
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

    return render(request, "books.html", context)

def book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book.html", {"book": book})

def delete_book(request, book_id):
    if request.method == "DELETE":
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=405)

def update_book_status(request, book_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_status = data.get('status')
            book = Book.objects.get(id=book_id)
            book.status = new_status
            book.save()
            return JsonResponse({'success': True}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def librarian(request):
    query = request.GET.get('q')
    genre_filter = request.GET.get('genre') 
    books = Book.objects.all()
    genres = Genre.objects.all()
    students = User.objects.all()

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

    return render(request, "librarian.html", context)
    
@login_required
def borrow_book(request, bookId):
    try:
        print(f"Received borrow request for bookId: {bookId}, User: {request.user}")

        book = Book.objects.get(bookId=bookId)
        print(f"Book found: {book.name}, Status: {book.status}")

        if book.status in ['Borrowed', 'Maintenance']:
            print(f"Book {book.name} is not available.")
            return JsonResponse({'message': 'Book not available'}, status=400)

        if Borrow.objects.filter(book=book, borrow_returned__isnull=True).exists():
            print(f"Book {book.name} is already borrowed by another user.")
            return JsonResponse({'message': 'Book already borrowed by someone else'}, status=400)

        borrow_record = Borrow.objects.create(
            book=book,
            user=request.user,
            borrow_date=timezone.now(),
            status='Borrowed'
        )
        print(f"Borrow record created for book: {book.name}, User: {request.user}")

        book.status = 'Borrowed'
        book.save()
        print(f"Book {book.name} status updated to 'Borrowed'.")

        return JsonResponse({'message': 'Book borrowed successfully'}, status=200)

    except ObjectDoesNotExist:
        print(f"Error: Book with id {bookId} not found.")
        return JsonResponse({'message': 'Book not found'}, status=404)
    except IntegrityError as e:
        print(f"Error: IntegrityError - {str(e)}")
        return JsonResponse({'message': f'Error with borrowing the book: {str(e)}'}, status=500)
    except Exception as e:
        error_message = traceback.format_exc()
        print(f"Full Exception Trace: {error_message}")
        return JsonResponse({'message': f'Error with borrowing the book: {str(e)}'}, status=500)