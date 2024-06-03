from classes.library import Library

def list_overdue_books(library: Library):
            overdue_books = library.list_overdue_books()
            if overdue_books:
                print('\033[96m' +"\nBorrowed overdue books:\n"+'\033[0m')
                for record in overdue_books:
                    print(f"{record.book_title} borrowed by {record.reader_name} was due on {record.return_date}")
       
            else:
                 print('\033[95m' +"\nNo overdue books."+'\033[0m' )        

