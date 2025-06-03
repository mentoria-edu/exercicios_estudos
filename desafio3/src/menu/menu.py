def show_display_menu():
    print("=== Menu ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("====================")

def execute_option():
    choice = input("Enter your choice: ")

    match choice:
        case '1':
            print("Adding Contact...")
            return False        
        case '2':
            print("Viewing Contact...")
            return False        
        case '3':
            print("Searching Contact...")
            return False
        case '4':
            print("Updating Contact...")
            return False
        case '5':
            print("Deleting Contact...")
            return False
        case '6':
            return True
        case _:
            print("Invalid option, check the options in the menu below")
            return False

def run_menu():        
    while True:
        show_display_menu()
        if execute_option():
            break
