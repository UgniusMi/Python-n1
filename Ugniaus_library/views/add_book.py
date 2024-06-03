from classes.library import Library

def add_book(library: Library):
    while True:
        title = input("Enter title: ")
        author = input("Enter author: ")
        while True:
            year_input = input("Enter year: ")
            if year_input.strip() == "":
                print("\nYou have not entered anything, please enter a year of book!\n")
                continue

            if not year_input.isdigit():
                print("\nWe can only enter numbers here.\n")
                continue
            
            year = int(year_input)
            if year <= 0:
                print("\nInvalid input! Year must be a positive integer.\n")
                continue
            break
        genre = input("Enter genre: ")
        while True:
            quantity_input = input("Enter quantity: ")
            if quantity_input.strip() == "":
                print("\nYou have not entered anything, please enter quantity of books you want to add.\n")
                continue

            if not quantity_input.isdigit():
                print("\nNumbers only!\n")
                continue

            quantity = int(quantity_input)
            if quantity <= 0:
                print("\nInvalid input! Quantity must be a positive integer.\n")
                continue
            break

        library.add_book(title, author, year, genre, quantity)
        print("\nBook added successfully.\n")
        break








# def add_book(library: Library):
#     while True:
#         year_input = input("Enter year: ")

#         if year_input.strip() == "":
#             print("Nieko neivedėte, prašome įvesti metus.")
#             continue

#         if not year_input.isdigit():
#             print("Čia galime vesti tik skaičius.")
#             continue

#         year = int(year_input)

#         if year <= 0:
#             print("Invalid input! Year must be a positive integer.")
#             continue

#         title = input("Enter title: ")
#         author = input("Enter author: ")
#         genre = input("Enter genre: ")
#         quantity = int(input("Enter quantity: "))
#         library.add_book(title, author, year, genre, quantity)
#         print("Book added successfully.")
#         break









# def  add_book(library: Library):
#     while True: 
#             title = input("Enter title: ")
#             author = input("Enter author: ")
#             year_input = input("Enter year: ")

#             if year_input.strip() == "":
#                 print("Nieko neivedėte, prašome įvesti metus")
#                 continue
#             if not year_input.isdigit():
#                   print("Invalid input! Year must be a number.")
#                 continue
            
#             year = int(year_input)

#             if year <=0:
#                 print("Invalid input! Year must be a positive integer.")
#                 continue
#             genre = input("Enter genre: ")
#             quantity = int(input("Enter quantity: "))
#             library.add_book(title, author, year, genre, quantity)
#             print("Book added successfully.")
#             break    