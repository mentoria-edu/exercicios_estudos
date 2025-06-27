from utils.logger import logger
from functools import wraps


def menu_loop(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            result = func(*args, **kwargs)

            if result == '9':
                break

        return result
      
    return wrapper


def show_display_main_menu():
    logger.info("=== Menu ===")
    logger.info("1. Add Contact")
    logger.info("2. View All Contacts")
    logger.info("3. Select Contact") 
    logger.info("9. Exit")
    logger.info("====================")


def show_display_contact_submenu():
    logger.info("=== Contact Menu ===")
    logger.info("1. Update Contact")
    logger.info("2. Delete Contact")
    logger.info("9. Return")
    logger.info("====================")


def show_display_get_serch():
    logger.info("Select the field to search by:")
    logger.info("1. Name")
    logger.info("2. Phone")
    logger.info("3. E-mail")


@menu_loop
def execute_main_menu() -> str:
    show_display_main_menu()

    choice = input("Enter your choice: ")

    match choice:
        case '1':            
            logger.info("Adding Contact...")                 
        case '2':
            logger.info("Viewing Contact...")                    
        case '3':
            logger.info("Selecting Contact...")
            get_search_contact()           
            execute_contact_submenu()       
        case '9':
            logger.info("Exiting...")
            return '9'
        case _:
            logger.warning("Invalid option, check the options in the menu below")
                        

@menu_loop
def execute_contact_submenu() -> str:
    show_display_contact_submenu()

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            logger.info("1. Update Contact")                  
        case '2':
            logger.info("2. Delete Contact")   
        case '9':
            logger.info("Returning...")
            return '9'
        case _:
            logger.warning("Invalid option, check the options in the menu below")


def get_field_search() -> str:
    while True:
        show_display_get_serch()

        choice = input("Choice:")

        match choice:            
            case '1':
                return 'name'
            case '2':
                return 'phone'             
            case '3':
                return 'email'      
            case _:
                logger.warning("Invalid option, check the options in the menu below")


def get_search_contact() -> tuple[str, str]:
    field = get_field_search()

    search_value = input("Search:").strip()

    return field, search_value


def run_menu():
    execute_main_menu()
