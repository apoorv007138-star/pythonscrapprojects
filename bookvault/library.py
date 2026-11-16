"""SQLite-backed library operations for BookVault."""
import csv
import sqlite3
from pathlib import Path


class LibraryManager:
    def __init__(self, database="bookvault.db"):
        self.database = str(database)
        self.connection = sqlite3.connect(self.database)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT UNIQUE,
                status TEXT NOT NULL DEFAULT 'available'
                    CHECK (status IN ('available', 'borrowed')),
                borrower TEXT,
                added_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.connection.commit()

    def add_book(self, title, author, isbn=None):
        title, author = title.strip(), author.strip()
        isbn = isbn.strip() if isbn and isbn.strip() else None
        if not title or not author:
            raise ValueError("Title and author are required.")
        try:
            cursor = self.connection.execute(
                "INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)",
                (title, author, isbn),
            )
            self.connection.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as exc:
            raise ValueError("That ISBN is already in your library.") from exc

    def list_books(self, status=None):
        if status not in (None, "available", "borrowed"):
            raise ValueError("Status must be available or borrowed.")
        if status:
            rows = self.connection.execute(
                "SELECT * FROM books WHERE status = ? ORDER BY title COLLATE NOCASE",
                (status,),
            )
        else:
            rows = self.connection.execute(
                "SELECT * FROM books ORDER BY title COLLATE NOCASE"
            )
        return rows.fetchall()

    def search_books(self, query):
        term = f"%{query.strip()}%"
        rows = self.connection.execute(
            """
            SELECT * FROM books
            WHERE title LIKE ? COLLATE NOCASE
               OR author LIKE ? COLLATE NOCASE
               OR isbn LIKE ? COLLATE NOCASE
            ORDER BY title COLLATE NOCASE
            """,
            (term, term, term),
        )
        return rows.fetchall()

    def borrow_book(self, book_id, borrower):
        borrower = borrower.strip()
        if not borrower:
            raise ValueError("Borrower name cannot be empty.")
        cursor = self.connection.execute(
            """
            UPDATE books SET status = 'borrowed', borrower = ?
            WHERE id = ? AND status = 'available'
            """,
            (borrower, book_id),
        )
        self.connection.commit()
        if cursor.rowcount == 0:
            raise ValueError("Book not found or it is already borrowed.")

    def return_book(self, book_id):
        cursor = self.connection.execute(
            """
            UPDATE books SET status = 'available', borrower = NULL
            WHERE id = ? AND status = 'borrowed'
            """,
            (book_id,),
        )
        self.connection.commit()
        if cursor.rowcount == 0:
            raise ValueError("Book not found or it is not currently borrowed.")

    def delete_book(self, book_id):
        cursor = self.connection.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.connection.commit()
        if cursor.rowcount == 0:
            raise ValueError("No book exists with that ID.")

    def get_stats(self):
        row = self.connection.execute(
            """
            SELECT COUNT(*) AS total,
                   SUM(CASE WHEN status = 'available' THEN 1 ELSE 0 END) AS available,
                   SUM(CASE WHEN status = 'borrowed' THEN 1 ELSE 0 END) AS borrowed
            FROM books
            """
        ).fetchone()
        return {
            "total": row["total"],
            "available": row["available"] or 0,
            "borrowed": row["borrowed"] or 0,
        }

    def export_csv(self, filename="books_export.csv"):
        rows = self.list_books()
        path = Path(filename)
        with path.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["ID", "Title", "Author", "ISBN", "Status", "Borrower", "Added At"])
            for book in rows:
                writer.writerow([
                    book["id"], book["title"], book["author"], book["isbn"] or "",
                    book["status"], book["borrower"] or "", book["added_at"],
                ])
        return path

    def close(self):
        self.connection.close()
