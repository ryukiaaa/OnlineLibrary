# Online Library

The Online Library is a web application built with Django that allows users to browse, borrow, and for the staff to manage books in a digital library. The application provides a user-friendly interface for both regular users and administrators to interact with library resources.

## Features Overview

### 1. Book Management
- Add, edit, and delete book records.
- Search and filter books by title, author, genre, or availability.
- View detailed information for each book.

### 2. User Management
- Maintain user profiles (members and administrators).
- Track borrowing history and account status.
- Admins can manage roles and permissions for users.

### 3. Borrowing System
- Users can borrow books based on availability.
- Track borrowed books and due dates.
- Send reminders for overdue books.

### 4. Book Reservation System
- Users can reserve books that are currently unavailable.
- Notifications when reserved books are available.

### 5. Book Categories and Genres
- Organize books into categories and genres.
- View and manage categories and genres.
- Browse books by category or genre.


## Tech Used

- **Backend**: Django (Python)
- **Database**: PostgreSQL (or any preferred database)
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Django's built-in authentication system
- **API**: Django REST Framework (if API endpoints are used)

## Documentation

- **UI/UX Design:** [View here](https://www.figma.com/design/pybJ8EehmIskXU07ULHOR7/BrainVault?node-id=0-1&t=pfe0Org42ogm2jzp-1)
- **ERD:** ![image](https://github.com/user-attachments/assets/de04f98f-7cfb-4cd6-95de-5dd93e0c5812)

## Installation

Follow these steps to get the project up and running on your local machine:

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django
- PostgreSQL (or your preferred database)

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/online-library.git
cd online-library
 ```
Apply the database migrations:

```bash
    python manage.py makemigrations
    python manage.py migrate
```
Create a superuser to access the Django admin interface:
```bash
    python manage.py createsuperuser
```
   Follow the prompts to enter a username, email, and password for the superuser.

Run the development server:
```bash
    python manage.py runserver
```
Access the admin interface by navigating to `{server}/admin` in your web browser and log in with your superuser account.
```bash
Update the role of the superuser as required.
```


