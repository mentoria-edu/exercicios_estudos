from src.validator import (
    get_valid_name,
    get_valid_phone,
    get_valid_email,
    confirm_data,
    infinite_try
)
from src.model import insert_database_row
from utils import logger
from src.model import search_rows_by_column
import sqlite3

def get_contact_informations(connector: sqlite3.Connection):
    name = get_valid_name()
    phone = get_valid_phone()
    email = get_valid_email()

    contact_infromation = (name, phone, email)
    validated_data = confirm_data(contact_infromation)
    insert_database_row(
            connector=connector,
            data=validated_data,
        )
    return validated_data


def _search_row(connector: sqlite3.Connection):
    field_choice = _get_menu_field_choice()
    field_values = input("Digite o valor que deseja buscar: ")

    options = search_rows_by_column(
            connector=connector,
            field=field_choice, 
            value=field_values
        )
    return options

def show_query_result(
        cursor_of_query: sqlite3.Cursor,
        id_column_name: str,
        select_columns: tuple[str,...]
        ):
    real_index = dict()
    
    for fake_index, item in enumerate(cursor_of_query, start=1):
        
        real_index[fake_index] = item[id_column_name]
        target_values = (item[column] for column in select_columns)
        
        values = (fake_index, *target_values)
        logger.info(values)
    

@infinite_try
def _get_menu_field_choice() -> str:

    _show_menu_field_choice()
    code_field_choice = input()

    match code_field_choice:
        case 1:
            return "name"
        case 2 :
            return "phone_number"
        case 3: 
            return "email"
        case 9:
            return 
        case _:
            logger.debug(f"O valor que o usuário inseriu: {code_field_choice}")
            raise ValueError("Por favor, insira um valor valido!")


def _show_menu_field_choice():
    logger.info("Selecione o campo que deseja buscar: ")
    logger.info("1 - Nome")
    logger.info("2 - Telefone")
    logger.info("3 - Email")
    logger.info("9 - Sair")
    

def _get_field_value():
    pass
        