from utils.logger import logger

def show_display_principal_menu():
    logger.info("=== Menu ===")    
    logger.info("1. Add Contact")
    logger.info("2. View All Contacts")
    logger.info("3. Select Contact")    
    logger.info("9. Exit")
    logger.info("====================")


def show_display_contact_menu():
    logger.info("=== Contact Menu ===")    
    logger.info("1. Update Contact")
    logger.info("2. Delete Contact")
    logger.info("9. Exit")   
    logger.info("====================")


def execute_principal_menu():
    show_display_principal_menu()

    choice = input("Enter your choice: ")

    match choice:
        case '1':            
            logger.info("Adding Contact...")                    
        case '2':
            logger.info("Viewing Contact...")                    
        case '3':
            logger.info("Selecting Contact...")
            loop_menu(execute_contact_menu)         
        case '9':
            logger.info("Exiting...")
            return 'exit'
        case _:
            logger.warning("Invalid option, check the options in the menu below")


def execute_contact_menu():
    show_display_contact_menu()

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            logger.info("1. Update Contact")                    
        case '2':
            logger.info("2. Delete Contact") 
        case '9':
            logger.info("Exiting...")
            return 'exit'
        case _:
            logger.warning("Invalid option, check the options in the menu below")


def loop_menu(menu_type):
    while True:
        control = menu_type()
        if control == 'exit':
            break
        

def run_menu():    
    loop_menu(execute_principal_menu)
