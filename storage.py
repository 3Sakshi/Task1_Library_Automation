import json
from pathlib import Path

from models import Book


DATA_FILE = Path(__file__).parent / "books.json"


def save_books(books):
    data = [
        {
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "available": book.available
        }
        for book in books
    ]

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_books():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            Book(
                book_id=item["book_id"],
                title=item["title"],
                author=item["author"],
                available=item.get("available", True)
            )
            for item in data
        ]

    except (json.JSONDecodeError, KeyError, TypeError):
        return []