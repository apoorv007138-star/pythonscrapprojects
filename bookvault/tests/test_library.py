"""Unit tests for BookVault's library operations."""
import tempfile
import unittest
from pathlib import Path

from library import LibraryManager


class LibraryManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        database = Path(self.temp_dir.name) / "test.db"
        self.library = LibraryManager(database)

    def tearDown(self):
        self.library.close()
        self.temp_dir.cleanup()

    def test_add_and_list_book(self):
        book_id = self.library.add_book("Atomic Habits", "James Clear", "ISBN-001")
        books = self.library.list_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["id"], book_id)
        self.assertEqual(books[0]["title"], "Atomic Habits")

    def test_search_by_author(self):
        self.library.add_book("Clean Code", "Robert Martin")
        results = self.library.search_books("robert")
        self.assertEqual(len(results), 1)

    def test_borrow_and_return_book(self):
        book_id = self.library.add_book("Python Basics", "A. Writer")
        self.library.borrow_book(book_id, "Sam")
        self.assertEqual(self.library.list_books()[0]["status"], "borrowed")
        self.library.return_book(book_id)
        self.assertEqual(self.library.list_books()[0]["status"], "available")

    def test_cannot_borrow_book_twice(self):
        book_id = self.library.add_book("Dune", "Frank Herbert")
        self.library.borrow_book(book_id, "Alex")
        with self.assertRaises(ValueError):
            self.library.borrow_book(book_id, "Taylor")

    def test_duplicate_isbn_is_rejected(self):
        self.library.add_book("Book One", "Author One", "123")
        with self.assertRaises(ValueError):
            self.library.add_book("Book Two", "Author Two", "123")

    def test_statistics(self):
        first = self.library.add_book("One", "Author")
        self.library.add_book("Two", "Author")
        self.library.borrow_book(first, "Jamie")
        self.assertEqual(
            self.library.get_stats(),
            {"total": 2, "available": 1, "borrowed": 1},
        )


if __name__ == "__main__":
    unittest.main()
