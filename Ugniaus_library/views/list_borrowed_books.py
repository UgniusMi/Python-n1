from classes.library import Library

def list_borrowed_books(library: Library):
            overdue_books = library.list_borrowed_books()
            print('\033[96m' +"\nAll borrowed books list:\n"+'\033[0m')
            for record in overdue_books:
                print(f"{record.book_title} borrowed by {record.reader_name} on {record.borrow_date}")