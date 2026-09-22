from library import Library


def test_add_book():
    library = Library()

    book = library.add_book(
        1,
        "Python Basics",
        "John Smith"
    )

    assert book.book_id == 1
    assert book.title == "Python Basics"
    assert book.author == "John Smith"
    assert book.available is True


def test_search_book():
    library = Library()
    library.add_book(1, "Python Basics", "John Smith")

    results = library.search_book("Python")

    assert len(results) == 1
    assert results[0].title == "Python Basics"


def test_issue_and_return_book():
    library = Library()
    library.add_book(1, "Python Basics", "John Smith")

    library.issue_book(1)
    assert library.books[0].available is False

    library.return_book(1)
    assert library.books[0].available is True


def test_delete_book():
    library = Library()
    library.add_book(1, "Python Basics", "John Smith")

    library.delete_book(1)

    assert len(library.books) == 0


def test_duplicate_book_id():
    library = Library()
    library.add_book(1, "Python Basics", "John Smith")

    try:
        library.add_book(1, "Another Book", "Another Author")
        assert False
    except ValueError:
        assert True