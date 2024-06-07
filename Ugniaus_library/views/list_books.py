from classes.library import Library

def list_books(library: Library):
            books = library.list_books()
            print('\033[96m' +"\nThe library has the following books:\n"+'\033[0m')
            for book in books:
                print(f"{book.title} by {book.author} ({book.year}) - {book.genre} available")