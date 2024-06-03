from views.add_book import add_book
from views.remove_old_books import remove_old_books
from views.borrow_book import borrow_book
from views.return_book import return_book
from views.search_books import search_books
from views.list_books import list_books
from views.list_overdue_books import list_overdue_books
from views.list_borrowed_books import list_borrowed_books



def menu(library):
    actions = {'1': add_book, 
                "2": remove_old_books, 
                "3": borrow_book,
                "4": return_book, 
                "5": search_books, 
                "6":list_books, 
                "7": list_overdue_books,
                "8": list_borrowed_books,
                }

    while True:
        print('\033[93m' +"\n----------------------------------\n Ugnius Library Management System\n---------------------------------- \n"+'\033[0m')
        print("1. Add new book")
        print("2. Remove old books")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Search books")
        print("6. List all books")
        print("7. List overdue books")
        print("8. List all borrowed books")
        print("9. Exit")

        choice = input('\033[92m' +"Choose an option: "+'\033[0m')
        if choice in actions:
            actions[choice](library)
        elif choice == '9':
            print('\033[91m' +"Exiting the program."+'\033[0m')
            break
        else:
            print('\033[91m' +"Invalid choice. Please try again."+'\033[0m')