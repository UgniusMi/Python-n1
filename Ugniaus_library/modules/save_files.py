import pickle

def save_books(books_file, books):
        with open(books_file, 'wb') as file:
            pickle.dump(books, file)

def save_records(records_file, borrow_records):
        with open(records_file, 'wb') as file:
            pickle.dump(borrow_records, file)            