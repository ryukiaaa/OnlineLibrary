from django.core.management.base import BaseCommand
from libManagement.models import Book, Author, Genre

class Command(BaseCommand):
    help = 'Insert predefined books into the database'

    def handle(self, *args, **kwargs):
        # Insert predefined genres if they do not exist
        genre_fantasy, created = Genre.objects.get_or_create(
            name="Fantasy", 
            description="Imaginative stories featuring magical elements, mythical creatures, or supernatural phenomena."
        )
        genre_scifi, created = Genre.objects.get_or_create(
            name="Science Fiction", 
            description="Stories exploring futuristic technology, space exploration, and the impact of science on society."
        )
        genre_mystery, created = Genre.objects.get_or_create(
            name="Mystery", 
            description="Intriguing narratives involving investigations, secrets, and solving crimes."
        )
        genre_romance, created = Genre.objects.get_or_create(
            name="Romance", 
            description="Tales focusing on love, relationships, and emotional connections."
        )
        genre_horror, created = Genre.objects.get_or_create(
            name="Horror", 
            description="Chilling stories designed to evoke fear, suspense, or dread."
        )
        genre_bio, created = Genre.objects.get_or_create(
            name="Biography", 
            description="Accounts of individuals’ lives, exploring their achievements and struggles."
        )
        genre_historical, created = Genre.objects.get_or_create(
            name="Historical Fiction",
            description="Stories set in the past, often incorporating real historical events and figures."
        )
        genre_young_adult, created = Genre.objects.get_or_create(
            name="Young Adult",
            description="Literature aimed at teenagers and young adults, dealing with coming-of-age themes."
        )

        # Insert predefined authors if they do not exist
        author_rowling, created = Author.objects.get_or_create(
            first_name="J.K.", 
            last_name="Rowling"
        )
        author_tolkien, created = Author.objects.get_or_create(
            first_name="J.R.R.", 
            last_name="Tolkien"
        )
        author_christie, created = Author.objects.get_or_create(
            first_name="Agatha", 
            last_name="Christie"
        )
        author_smith, created = Author.objects.get_or_create(
            first_name="Will", 
            last_name="Smith"
        )
        
        # Predefined list of books
        books = [
            {
                'bookId': '12345',
                'name': 'Harry Potter and the Sorcerer\'s Stone',
                'publisher': 'Bloomsbury',
                'year_published': 1997,
                'edition': '1st',
                'synopsis': 'A young boy discovers he is a wizard and attends a magical school.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_fantasy,
                'author': author_rowling,
            },
            {
                'bookId': '67890',
                'name': 'The Hobbit',
                'publisher': 'HarperCollins',
                'year_published': 1937,
                'edition': '1st',
                'synopsis': 'A hobbit embarks on a journey to reclaim treasure from a dragon.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_fantasy,
                'author': author_tolkien,
            },
            {
                'bookId': '11121',
                'name': 'Murder on the Orient Express',
                'publisher': 'Collins Crime Club',
                'year_published': 1934,
                'edition': '1st',
                'synopsis': 'A detective solves a murder mystery aboard a train.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_mystery,
                'author': author_christie,
            },
            {
                'bookId': '54321',
                'name': 'The Pursuit of Happyness',
                'publisher': 'Amistad',
                'year_published': 2006,
                'edition': '1st',
                'synopsis': 'The inspiring true story of Chris Gardner’s rise from homelessness.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_bio,
                'author': author_smith,
            },
            {
                'bookId': '22222',
                'name': 'The Lord of the Rings: The Fellowship of the Ring',
                'publisher': 'HarperCollins',
                'year_published': 1954,
                'edition': '1st',
                'synopsis': 'A group of heroes sets out to destroy a powerful ring that could endanger Middle-earth.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_fantasy,
                'author': author_tolkien,
            },
            {
                'bookId': '33333',
                'name': 'The Catcher in the Rye',
                'publisher': 'Little, Brown and Company',
                'year_published': 1951,
                'edition': '1st',
                'synopsis': 'A teenager struggles with alienation and finding his place in the world.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_young_adult,
                'author': author_christie,
            },
            {
                'bookId': '44444',
                'name': '1984',
                'publisher': 'Secker & Warburg',
                'year_published': 1949,
                'edition': '1st',
                'synopsis': 'A dystopian society is controlled by a totalitarian government that suppresses free thought.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_scifi,
                'author': author_christie,
            },
            {
                'bookId': '55555',
                'name': 'The Great Gatsby',
                'publisher': 'Charles Scribner\'s Sons',
                'year_published': 1925,
                'edition': '1st',
                'synopsis': 'A young man navigates love, wealth, and the pursuit of the American Dream in the 1920s.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_romance,
                'author': author_christie,
            },
            {
                'bookId': '66666',
                'name': 'Pride and Prejudice',
                'publisher': 'T. Egerton, Whitehall',
                'year_published': 1813,
                'edition': '1st',
                'synopsis': 'A spirited young woman navigates issues of class, marriage, and morality in Regency-era England.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_romance,
                'author': author_rowling,
            },
            {
                'bookId': '77777',
                'name': 'The Shining',
                'publisher': 'Doubleday',
                'year_published': 1977,
                'edition': '1st',
                'synopsis': 'A man begins to unravel as he and his family are trapped in a haunted hotel.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_horror,
                'author': author_christie,
            },
            {
                'bookId': '88888',
                'name': 'A Game of Thrones',
                'publisher': 'Bantam Books',
                'year_published': 1996,
                'edition': '1st',
                'synopsis': 'Noble families vie for control of the Iron Throne in a brutal, medieval-inspired world.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_fantasy,
                'author': author_tolkien,
            },
            {
                'bookId': '99999',
                'name': 'Brave New World',
                'publisher': 'Chatto & Windus',
                'year_published': 1932,
                'edition': '1st',
                'synopsis': 'A society strives for stability through mass production, control, and elimination of individual freedom.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_scifi,
                'author': author_christie,
            },
            {
                'bookId': '101010',
                'name': 'Wuthering Heights',
                'publisher': 'Thomas Newby',
                'year_published': 1847,
                'edition': '1st',
                'synopsis': 'A passionate, destructive love story set on the moors of England.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_romance,
                'author': author_rowling,
            },
            {
                'bookId': '112233',
                'name': 'Frankenstein',
                'publisher': 'Lackington, Hughes, Harding, Mavor & Jones',
                'year_published': 1818,
                'edition': '1st',
                'synopsis': 'A scientist creates a monster in an experiment gone horribly wrong.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_horror,
                'author': author_christie,
            },
            {
                'bookId': '223344',
                'name': 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe',
                'publisher': 'Geoffrey Bles',
                'year_published': 1950,
                'edition': '1st',
                'synopsis': 'Four children step into a magical world where they fight against evil forces.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_fantasy,
                'author': author_tolkien,
            },
            {
                'bookId': '334455',
                'name': 'The Odyssey',
                'publisher': 'Penguin Classics',
                'year_published': 2005,
                'edition': '1st',
                'synopsis': 'The epic journey of Odysseus as he attempts to return home after the Trojan War.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_romance,
                'author': author_rowling,
            },
            {
                'bookId': '445566',
                'name': 'The Da Vinci Code',
                'publisher': 'Doubleday',
                'year_published': 2003,
                'edition': '1st',
                'synopsis': 'A symbologist uncovers a religious mystery that threatens the fabric of Christianity.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_mystery,
                'author': author_rowling,
            },
            {
                'bookId': '556677',
                'name': 'To Kill a Mockingbird',
                'publisher': 'J.B. Lippincott & Co.',
                'year_published': 1960,
                'edition': '1st',
                'synopsis': 'A young girl learns about racial injustice in the Deep South during the Great Depression.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_historical,
                'author': author_rowling,
            },
            {
                'bookId': '667788',
                'name': 'The Girl with the Dragon Tattoo',
                'publisher': 'Norstedts Förlag',
                'year_published': 2005,
                'edition': '1st',
                'synopsis': 'A journalist teams up with a hacker to solve a decades-old disappearance.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_mystery,
                'author': author_rowling,
            },
            {
                'bookId': '778899',
                'name': 'The Secret Garden',
                'publisher': 'Frederick A. Stokes Company',
                'year_published': 1911,
                'edition': '1st',
                'synopsis': 'A young orphan transforms a neglected garden and her life.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_young_adult,
                'author': author_rowling,
            },
            {
                'bookId': '889900',
                'name': 'The Fault in Our Stars',
                'publisher': 'Dutton Books',
                'year_published': 2012,
                'edition': '1st',
                'synopsis': 'Two teenagers with cancer fall in love and confront their mortality.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_romance,
                'author': author_rowling,
            },
            {
                'bookId': '990011',
                'name': 'The Road',
                'publisher': 'Knopf',
                'year_published': 2006,
                'edition': '1st',
                'synopsis': 'A father and son struggle to survive in a post-apocalyptic world.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_scifi,
                'author': author_rowling,
            },
            {
                'bookId': '100122',
                'name': 'The Hunger Games',
                'publisher': 'Scholastic Press',
                'year_published': 2008,
                'edition': '1st',
                'synopsis': 'A girl must fight for survival in a televised competition in a dystopian future.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_scifi,
                'author': author_rowling,
            },
            {
                'bookId': '101233',
                'name': 'Gone with the Wind',
                'publisher': 'Macmillan Publishers',
                'year_published': 1936,
                'edition': '1st',
                'synopsis': 'A woman survives the Civil War and its aftermath while navigating love and loss.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_romance,
                'author': author_rowling,
            },
            {
                'bookId': '102344',
                'name': 'Dune',
                'publisher': 'Chilton Books',
                'year_published': 1965,
                'edition': '1st',
                'synopsis': 'A young man becomes embroiled in a galactic conflict over a valuable resource.',
                'status': 'Available',
                'book_type': 'Paperback',
                'genre': genre_scifi,
                'author': author_rowling,
            },
            {
                'bookId': '103455',
                'name': 'The Bell Jar',
                'publisher': 'Harper & Row',
                'year_published': 1963,
                'edition': '1st',
                'synopsis': 'A young woman struggles with depression while trying to find her place in society.',
                'status': 'Available',
                'book_type': 'Hardcover',
                'genre': genre_romance,
                'author': author_rowling,
            }
        ]

        # Insert books into the database
        for book_data in books:
            # Check if the bookId already exists in the database
            if not Book.objects.filter(bookId=book_data['bookId']).exists():
                Book.objects.create(
                    bookId=book_data['bookId'],
                    name=book_data['name'],
                    publisher=book_data['publisher'],
                    year_published=book_data['year_published'],
                    edition=book_data['edition'],
                    synopsis=book_data['synopsis'],
                    status=book_data['status'],
                    book_type=book_data['book_type'],
                    genre=book_data['genre'],
                    author=book_data['author'],
                )
            else:
                print(f"Book with bookId {book_data['bookId']} already exists. Skipping.")