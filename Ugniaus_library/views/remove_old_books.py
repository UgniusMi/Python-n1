from classes.library import Library
   

def remove_old_books(library: Library):
    try:
        age_limit = int(input("Enter the age limit in years to remove old books: "))
    except ValueError:
        print('\033[91m' +"Invalid input! Please enter a valid number."+'\033[0m' )
        return

    library.remove_old_books(age_limit)
    print('\033[95m' +f"\nAll books older than {age_limit} years removed successfully."+'\033[0m' )       