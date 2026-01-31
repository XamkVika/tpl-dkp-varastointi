import pytest
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from db.database import create_db, add_data, query_data, DB_PATH

@pytest.fixture(autouse=True)
def setup_db(tmp_path):
    # Use a temporary database file inside pytest tmp_path
    test_db_path = tmp_path / "test_books.db"
    import db.database as database
    database.DB_PATH = test_db_path

    create_db()
    yield

def test_query_returns_books():
    books = {
        "War and Peace": {"author": "Leo Tolstoy", "pages": 1225},
        "1984": {"author": "George Orwell", "pages": 328},
        "Moby Dick": {"author": "Herman Melville", "pages": 635},
    }

    add_data(books)
    results = query_data(2)

    # Check that we got some rows
    assert len(results) > 0

    # Check that the first returned row is one of the inserted books
    titles = [row[0] for row in results]
    for title in titles:
        assert title in books
