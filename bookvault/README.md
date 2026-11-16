# BookVault – Personal Library Manager

BookVault is a beginner-friendly Python project for managing a personal book collection. It runs in the terminal and stores data in an SQLite database, so your books remain saved after you close the program.

## Features

- Add books with title, author, and optional ISBN
- View all books and search by title, author, or ISBN
- Track available and borrowed books
- Record who borrowed a book and process returns
- Delete books from the collection
- View library statistics
- Export the collection to a CSV file
- SQLite storage; no external packages required

## Requirements

- Python 3.8 or newer
- No third-party dependencies (SQLite is included with Python)

## Run the project

1. Download or clone this repository.
2. Open a terminal in the `bookvault` folder.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

The program creates `bookvault.db` automatically the first time it runs. Your data is stored locally in that file.

## Run the tests

From inside the `bookvault` folder, run:

```bash
python -m unittest discover -s tests -v
```

The tests use temporary databases and do not change your personal library.

## Project structure

```text
bookvault/
├── main.py              # Interactive terminal menu
├── library.py           # SQLite database and library operations
├── README.md            # Setup and usage guide
└── tests/
    └── test_library.py  # Automated unit tests
```

## Example workflow

1. Choose **1** to add a book.
2. Choose **2** to view your collection and note a book's ID.
3. Choose **4** to lend it to someone.
4. Choose **5** when it is returned.
5. Choose **7** to see your library statistics.
6. Choose **8** to export your collection to CSV.

## Notes

- ISBN values must be unique when provided.
- A book cannot be borrowed if it is already marked as borrowed.
- The database is local to your computer. Do not delete `bookvault.db` if you want to keep your saved collection.
