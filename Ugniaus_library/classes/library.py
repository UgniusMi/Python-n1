from datetime import date, timedelta, datetime
from classes.book import Book
from classes.reader import Reader
from modules.load_files import load_books, load_reader_records
from modules.save_files import *
# from modules.book_actions import *

class Library:
    def __init__(self, books_file="Ugniaus_library\\Documents\\books.pkl", records_file='Ugniaus_library\\Documents\\records.pkl'):
        self.books_file = books_file
        self.records_file = records_file
        self.books = load_books(self.books_file)
        self.reader_records = load_reader_records(records_file)

   
    def add_book(self, title, author, year, genre, quantity):
        new_book = Book(title, author, year, genre, quantity)
        self.books.append(new_book)
        save_books(self.books_file, self.books)
    
    def remove_old_books(self, age_limit):
        current_year = date.today().year
        self.books = [book for book in self.books if current_year - book.year <= age_limit]

        save_books(self.books_file, self.books)
   

    def borrow_book(self, title, reader_name, borrow_days=14):
        for book in self.books:
            if book.title == title and book.quantity > 0:
                for record in self.reader_records:
                    if record.reader_name == reader_name and record.is_overdue():
                        return '\033[91m'+"Cannot borrow. You have overdue books."+'\033[0m'
                return_date = datetime.now().date() + timedelta(days=borrow_days)
                # return_date = datetime.now().date() - timedelta(days=borrow_days)
                new_record = Reader(title, reader_name, datetime.now().date().strftime("%Y-%m-%d"), return_date.strftime("%Y-%m-%d"))
                self.reader_records.append(new_record) 
                book.quantity -= 1
                save_books(self.books_file, self.books)
                save_records(self.records_file, self.reader_records)
                return '\033[92m'+ f"Book borrowed successfully. Return by {return_date}."+'\033[0m'
        return "\n\U0001F47D  Book not available. \U0001F47D"

    def return_book(self, title, reader_name):
        for record in self.reader_records:
            if record.book_title == title and record.reader_name == reader_name:
                self.reader_records.remove(record)
                for book in self.books:
                    if book.title == title:
                        book.quantity += 1
                        break
                save_books(self.books_file, self.books)
                save_records(self.records_file, self.reader_records)
                return "Book returned successfully."
        return "You have entered an incorrect name or book title."

    def search_books(self, search):
        return [book for book in self.books if search.lower() in book.title.lower() or search.lower() in book.author.lower()]

    def list_books(self):
        return self.books

    def list_overdue_books(self):
        return [record for record in self.reader_records if record.is_overdue()]
    
    def list_borrowed_books(self):
        return [record for record in self.reader_records]