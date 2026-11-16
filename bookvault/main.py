"""Interactive command-line interface for BookVault."""
from library import LibraryManager


def show_books(books):
    if not books:
        print("\nNo books found.")
        return
    print("\n" + "-" * 78)
    print(f"{'ID':<5} {'TITLE':<28} {'AUTHOR':<20} {'STATUS':<12} BORROWER")
    print("-" * 78)
    for book in books:
        title = book["title"][:26]
        author = book["author"][:18]
        borrower = book["borrower"] or "-"
        print(f"{book['id']:<5} {title:<28} {author:<20} {book['status']:<12} {borrower}")
    print("-" * 78)


def main():
    library = LibraryManager()
    menu = """
========== BOOKVAULT ==========
1. Add a book
2. View all books
3. Search books
4. Borrow a book
5. Return a book
6. Delete a book
7. View library statistics
8. Export books to CSV
0. Exit
"""

    try:
        while True:
            print(menu)
            choice = input("Choose an option: ").strip()

            try:
                if choice == "1":
                    title = input("Book title: ")
                    author = input("Author: ")
                    isbn = input("ISBN (optional): ")
                    book_id = library.add_book(title, author, isbn)
                    print(f"Book added successfully! ID: {book_id}")

                elif choice == "2":
                    show_books(library.list_books())

                elif choice == "3":
                    query = input("Search by title, author, or ISBN: ")
                    show_books(library.search_books(query))

                elif choice == "4":
                    book_id = int(input("Book ID: "))
                    borrower = input("Borrower's name: ")
                    library.borrow_book(book_id, borrower)
                    print("Book marked as borrowed.")

                elif choice == "5":
                    book_id = int(input("Book ID to return: "))
                    library.return_book(book_id)
                    print("Book returned successfully.")

                elif choice == "6":
                    book_id = int(input("Book ID to delete: "))
                    library.delete_book(book_id)
                    print("Book deleted.")

                elif choice == "7":
                    stats = library.get_stats()
                    print("\nLibrary statistics")
                    print(f"Total books:     {stats['total']}")
                    print(f"Available:       {stats['available']}")
                    print(f"Currently lent:  {stats['borrowed']}")

                elif choice == "8":
                    filename = input("CSV filename (press Enter for books_export.csv): ").strip()
                    path = library.export_csv(filename or "books_export.csv")
                    print(f"Export saved to: {path.resolve()}")

                elif choice == "0":
                    print("Thanks for using BookVault. Goodbye!")
                    break

                else:
                    print("Please choose a valid menu option.")

            except ValueError as error:
                print(f"Could not complete that action: {error}")

            except OSError as error:
                print(f"File error: {error}")

    except (KeyboardInterrupt, EOFError):
        print("\nExiting BookVault...")
    finally:
        library.close()


if __name__ == "__main__":
    main()
