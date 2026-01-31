# SQL with SQLite Exercise

Your goal is to practice basic database operations in Python using SQLite.

You will:
Create a database and a table for storing book data.
Insert books (from a given dictionary) into the table.
Query books back from the database.

Project Structure
```
/
│
├── db/
│   └── database.py      # TODOs: implement create_db, add_data, query_data
│
├── data/
│   └── (sqlite_books.db will be created here)
│
├── tests/
│   └── test_database.py # automated tests
│
├── main.py              # TODOs. Entry point to run your code
└── requirements.txt     # includes pytest
```

## Instructions
1. Clone this repository.
2. Create and activate a virtual environment and install requirements

in [Visual Studio Code](https://code.visualstudio.com/docs/python/environments#_creating-environments), select the requirements.txt file when prompted for dependecies

OR

in cmd:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Open main.py and database.py and follow the detailed tasks inside the files.

4. To test and run your code, just run the `main.py`. Make sure that you have the correct Python environment in use.

5. In this project and GitHub Classroom assignment we are using also tests. You can run the tests in the cmd in the project root with:
`python -m pytest`

6. Commit and push your changes to this repository.
