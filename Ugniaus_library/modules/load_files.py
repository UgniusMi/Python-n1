import pickle


import sqlite3

conn = sqlite3.connect("Ugniaus_library\\data\\library_data.db")
c = conn.cursor()


def load_books():
    try:
        # c.execute("Select * FROM Book")
        books = c.execute("Select * FROM Book").fetchall()
        return books
    
    except FileNotFoundError:
                    return []

# books = c.execute("Select * FROM Book").fetchall()    




# def load_books(books_file):
#         try:
#             with open(books_file, 'rb') as file:
#                 books = pickle.load(file)
#                 return books

#         except FileNotFoundError:
#             return []
        
def load_reader_records(records_file):
        try:
             with open(records_file, 'rb') as file:
                records = pickle.load(file)
                return records
        except FileNotFoundError:
            return []