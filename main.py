from library import Library
from storage import load_books, save_books


def display_books(books):
    if not books:
        print("\nNo books found.")
        return

    print("\n--- Library Books ---")
    for book in books:
        status = "Available" if book.available else "Issued"
        print(
            f"ID: {book.book_id} | "
            f"Title: {book.title} | "
            f"Author: {book.author} | "
            f"Status: {status}"
        )


def get_book_id():
    while True:
        try:
            return int(input("Enter book ID: ").strip())
        except ValueError:
            print("Invalid input. Book ID must be a number.")


def add_book(library):
    try:
        book_id = get_book_id()
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()

        book = library.add_book(book_id, title, author)
        save_books(library.books)

        print(f"Book '{book.title}' added successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def search_book(library):
    keyword = input("Enter title or author to search: ").strip()

    try:
        results = library.search_book(keyword)
        display_books(results)
    except ValueError as error:
        print(f"Error: {error}")


def issue_book(library):
    try:
        book_id = get_book_id()
        book = library.issue_book(book_id)
        save_books(library.books)

        print(f"Book '{book.title}' issued successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def return_book(library):
    try:
        book_id = get_book_id()
        book = library.return_book(book_id)
        save_books(library.books)

        print(f"Book '{book.title}' returned successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def delete_book(library):
    try:
        book_id = get_book_id()
        book = library.delete_book(book_id)
        save_books(library.books)

        print(f"Book '{book.title}' deleted successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def main():
    library = Library(load_books())

    while True:
        print("\n========== Library Automation Tool ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        print("=============================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_book(library)

        elif choice == "2":
            display_books(library.get_all_books())

        elif choice == "3":
            search_book(library)

        elif choice == "4":
            issue_book(library)

        elif choice == "5":
            return_book(library)

        elif choice == "6":
            delete_book(library)

        elif choice == "7":
            print("Thank you for using Library Automation Tool.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()