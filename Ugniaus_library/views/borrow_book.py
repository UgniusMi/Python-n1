from classes.library import Library

def borrow_book(library: Library):
            title = input("Enter book title: ")
            reader_name = input("Enter your name: ")
            result = library.borrow_book(title, reader_name)
            print(result)