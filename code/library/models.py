class Librarian:
    def __init__(self, first_name, last_name, email, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary

    def __str__(self):
        return f"Librarian: {self.first_name} {self.last_name}, Email: {self.email}"

class User:
    def __init__(self, first_name, last_name, email, active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.active = active
        self.borrowed_book = None

    def __str__(self):
        return f"User: {self.first_name} {self.last_name}, Email: {self.email}, Active: {self.active}"

    def borrow_book(self, book):
        if book.is_taken:
            return False
        self.borrowed_book = book
        book.is_taken = True
        return True

    def return_book(self):
        if self.borrowed_book:
            self.borrowed_book.is_taken = False
            self.borrowed_book = None

class Category:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        return f"Category: {self.name}, Books: {len(self.books)}"

    def add_book(self, book):
        self.books.append(book)

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_taken = False

    def __str__(self):
        return f"Book: {self.title} by {self.author}, Category: {self.category}, Taken: {self.is_taken}"