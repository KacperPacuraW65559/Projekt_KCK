import sqlite3

connection = sqlite3.connect('database.db')

with connection:
    connection.execute("""
        CREATE TABLE lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            bookmarked INTEGER DEFAULT 0,
            completed INTEGER DEFAULT 0
        );
    """)

    lessons = [
        ("Lekcja 1", "Wstęp do nauki gry"),
        ("Lekcja 2", "Kostkowanie naprzemienne"),
        ("Lekcja 3", "Zaawansowane techniki gry")
    ]

    connection.executemany("INSERT INTO lessons (name, description) VALUES (?, ?);", lessons)

print("Baza danych utworzona poprawnie.")

connection.close()