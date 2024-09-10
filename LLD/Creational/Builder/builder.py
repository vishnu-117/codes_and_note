class Book:
    def __init__(self):
        self.title = None
        self.author = None
        self.isbn = None
        self.publisher = None
        self.year = None

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Publisher: {self.publisher}, Year: {self.year}"

class BookBuilder:
    def __init__(self):
        self.book = Book()

    def set_title(self, title):
        self.book.title = title
        return self

    def set_author(self, author):
        self.book.author = author
        return self

    def set_isbn(self, isbn):
        self.book.isbn = isbn
        return self

    def set_publisher(self, publisher):
        self.book.publisher = publisher
        return self

    def set_year(self, year):
        self.book.year = year
        return self

    def build(self):
        return self.book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)

# Usage
library = Library()

book1 = (BookBuilder()
         .set_title("The Catcher in the Rye")
         .set_author("J.D. Salinger")
         .set_isbn("978-0-316-76948-0")
         .set_publisher("Little, Brown and Company")
         .set_year(1951)
         .build())

book2 = (BookBuilder()
         .set_title("To Kill a Mockingbird")
         .set_author("Harper Lee")
         .set_isbn("978-0-06-112008-4")
         .set_publisher("J.B. Lippincott & Co.")
         .set_year(1960)
         .build())

library.add_book(book1)
library.add_book(book2)

library.show_books()
