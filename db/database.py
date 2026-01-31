import sqlite3
from pathlib import Path

DB_PATH = Path("sqlite_books.db")

def create_db():
    """
    TODO: Implement a function that:
      - Connects to the database (sqlite3.connect)
      - Creates a table 'books' with columns:
          id (INTEGER PRIMARY KEY AUTOINCREMENT),
          title (TEXT, not null),
          author (TEXT, not null),
          pages (INTEGER, not null)
      - Closes the connection

      - Remove the "pass", it's just to avoid syntax errors for now
    """
    pass


def add_data(books_dict):
    """
    TODO: Implement a function that:
      - Connects to the database
      - Iterates through the dictionary {title: {author, pages}}
      - Inserts each book into the 'books' table
      - Commits changes and closes the connection
    Example insert:
        cursor.execute(
            "INSERT INTO books (title, author, pages) VALUES (?, ?, ?)",
            (title, info["author"], info["pages"])
        )

      - Remove the "pass", it's just to avoid syntax errors for now
    """
    pass


def query_data(limit):
    """
    TODO: Implement a function that:
      - Connects to the database
      - Executes a query to select 'title, author, pages'
        ordered by 'pages' descending
      - Limits the result set to the given 'limit'
      - Closes the connection

      - Returns the rows
      
      - Remove the "pass", it's just to avoid syntax errors for now
    """
    pass