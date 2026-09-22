def validate_book_id(book_id):
    if not isinstance(book_id, int) or book_id <= 0:
        raise ValueError("Book ID must be a positive integer.")
    return book_id

def validate_text(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")
    return value.strip()

def validate_title(title):
    return validate_text(title, "Title")

def validate_author(author):
    return validate_text(author, "Author")