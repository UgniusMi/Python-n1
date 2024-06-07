import pickle

import sqlite3

conn = sqlite3.connect("Ugniaus_library\\data\\library_data.db")
c = conn.cursor()

def save_books(book):
    with conn:
         c.execute("INSERT INTO Book (title, author, year, genre) VALUES (?,?,?,?)", (book.title, book.author, book.year, book.genre))


# def save_books(books_file, books):
        # with open(books_file, 'wb') as file:
        #     pickle.dump(books, file)

          
def save_records(records_file, borrow_records):
        with open(records_file, 'wb') as file:
            pickle.dump(borrow_records, file)            