import pickle

def load_books(books_file):
        try:
            with open(books_file, 'rb') as file:
                books = pickle.load(file)
                return books

        except FileNotFoundError:
            return []
        
def load_reader_records(records_file):
        try:
             with open(records_file, 'rb') as file:
                records = pickle.load(file)
                return records
        except FileNotFoundError:
            return []