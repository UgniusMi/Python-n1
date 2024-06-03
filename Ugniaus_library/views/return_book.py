from classes.library import Library

def return_book(library: Library):
            title = input("Enter book title: ")
            reader_name = input("Enter your name: ")
            result = library.return_book(title, reader_name)
            print(result)