from utils.logger import logger
from functools import wraps


QUIT_OPTION = 'q'
KEEP_LOOP = 'keep'


def menu_loop(display_func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                if display_func:
                    display_func()

                choice = input(f"Enter your choice (or '{QUIT_OPTION}' to quit/return): ").strip()

                if choice == QUIT_OPTION:
                    break

                func(choice, *args, **kwargs)                                      

        return wrapper
    
    return decorator

def unique_choose_loop(display_func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):     
            while True:
                if display_func:
                    display_func()            

                result = func(*args, **kwargs)

                if result != KEEP_LOOP:               
                    return result                             

        return wrapper
    
    return decorator


def show_display_main_menu():
    logger.info("=== Menu ===")
    logger.info("1. Add Contact")
    logger.info("2. View All Contacts")
    logger.info("3. Select Contact") 
    logger.info(f"{QUIT_OPTION}. Exit")
    logger.info("====================")


def show_display_contact_submenu():
    logger.info("=== Contact Menu ===")
    logger.info("1. Update Contact")
    logger.info("2. Delete Contact")
    logger.info(f"{QUIT_OPTION}. Return")
    logger.info("====================")


def show_display_choose_field_to_search():
    logger.info("=== Select the field to search by ====")
    logger.info("1. Name")
    logger.info("2. Phone")
    logger.info("3. E-mail")
    logger.info("==============")


@menu_loop(display_func=show_display_main_menu)
def execute_main_menu(choice):
    match choice:
        case '1':
            logger.info("Adding Contact...")
        case '2':
            logger.info("Viewing Contact...")                
        case '3':
            logger.info("Selecting Contact...")
            select_search_contact()
            execute_contact_submenu()
        case _:
            logger.warning("Invalid option, check the options in the menu below")
                        

@menu_loop(display_func=show_display_contact_submenu)
def execute_contact_submenu(choice):
    match choice:
        case '1':
            logger.info("1. Update Contact")         
        case '2':
            logger.info("2. Delete Contact")    
        case _:
            logger.warning("Invalid option, check the options in the menu below")


@unique_choose_loop(display_func=show_display_choose_field_to_search)
def _choose_field_to_search() -> str:

    choice = input("Choice: ")

    match choice:        
        case '1':
            return 'name'
        case '2':
            return 'phone'         
        case '3':
            return 'email'
        case _:
            logger.warning("Invalid option, check the options in the menu below")
            return KEEP_LOOP


def select_search_contact() -> tuple[str, str]:
    field = _choose_field_to_search()

    search_value = input("Search:").strip()

    return field, search_value


def run_menu():
    execute_main_menu()
