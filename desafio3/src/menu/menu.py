from src.button.button import get_contact_information
from src.model.model import insert_database_row

def display_menu():
    print("=== Menu Inicial ===")
    print("1. Opção 1 - Descrição da opção 1")
    print("2. Opção 2 - Descrição da opção 2")
    print("3. Opção 3 - Descrição da opção 3")
    print("4. Sair")
    print("====================")


def menu_options():
    while True:
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Adding a contact...")
            contact_information = get_contact_information()
            insert_database_row(contact_information)
        elif choice == '2':
            print("Viewing contacts...")
            # View contacts logic here
        elif choice == '3':
            print("Searching for a contact...")
            # Search contact logic here
        elif choice == '4':
            print("Dceleting a ontact...")
            # Delete contact logic here
        elif choice == '5':
            print("Exiting the program.")
            break


def run_menu():
    display_menu()
    menu_options()
