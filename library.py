from models import Book
from validators import (
    validate_book_id,
    validate_title,
    validate_author
)


class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def add_book(self, book_id, title, author):
        validate_book_id(book_id)
        validate_title(title)
        validate_author(author)

        if any(book.book_id == book_id for book in self.books):
            raise ValueError("A book with this ID already exists.")

        book = Book(book_id, title.strip(), author.strip())
        self.books.append(book)
        return book

    def get_all_books(self):
        return self.books

    def search_book(self, keyword):
        keyword = validate_title(keyword).lower()

        return [
            book for book in self.books
            if keyword in book.title.lower()
            or keyword in book.author.lower()
        ]

    def issue_book(self, book_id):
        validate_book_id(book_id)

        book = self._find_book(book_id)

        if book is None:
            raise ValueError("Book not found.")

        if not book.available:
            raise ValueError("Book is already issued.")

        book.available = False
        return book

    def return_book(self, book_id):
        validate_book_id(book_id)

        book = self._find_book(book_id)

        if book is None:
            raise ValueError("Book not found.")

        if book.available:
            raise ValueError("Book is already available.")

        book.available = True
        return book

    def delete_book(self, book_id):
        validate_book_id(book_id)

        book = self._find_book(book_id)

        if book is None:
            raise ValueError("Book not found.")

        self.books.remove(book)
        return book

    def _find_book(self, book_id):
        return next(
            (book for book in self.books if book.book_id == book_id),
            None
        )