#TODO: import pandas
from db.database import create_db, add_data, query_data

def main():

    books = {
        "War and Peace": {"author": "Leo Tolstoy", "pages": 1225},
        "1984": {"author": "George Orwell", "pages": 328},
        "Moby Dick": {"author": "Herman Melville", "pages": 635},
        "Ulysses": {"author": "James Joyce", "pages": 730},
        "The Great Gatsby": {"author": "F. Scott Fitzgerald", "pages": 180},
        "Don Quixote": {"author": "Miguel de Cervantes", "pages": 1072},
        "The Brothers Karamazov": {"author": "Fyodor Dostoevsky", "pages": 824},
        "Crime and Punishment": {"author": "Fyodor Dostoevsky", "pages": 671},
        "The Hobbit": {"author": "J.R.R. Tolkien", "pages": 310},
        "Pride and Prejudice": {"author": "Jane Austen", "pages": 279}
    }

    # TODO: 1. Call create_db() to initialize the database

    # TODO: 2. Call add_data() function with books as a parameter to insert the books into the database

    # TODO: 3. Call query_data() to fetch 5 first books in to a dataframe with columns: title, author, pages
    # print the dataframe to the console


if __name__ == "__main__":
    main()