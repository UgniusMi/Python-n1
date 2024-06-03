from classes.library import Library

def search_books(library: Library):
    search = input("Enter the title or author: ")
    results = library.search_books(search)
    if results:
        print('\033[96m' +"\nWe found the following books with the title/author you specified:\n"+'\033[0m')
        for book in results:
            print(f"{book.title} by {book.author} ({book.year}) - {book.genre} - {book.quantity} available")
             
    else:
            print('\033[91m' +"\nCould not find any book with this title or author."+'\033[0m' )
             