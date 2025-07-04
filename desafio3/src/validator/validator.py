from functools import wraps
from utils import logger
from typing import Callable


# def infinite_try(validation_function: Callable) -> Callable:
#     @wraps(validation_function)
#     def wrapper(*args):
#         while True:
#             try:
#                 return validation_function(*args)
#             except Exception as msg_error:
#                 logger.info(msg_error)
#     return wrapper


def infinite_try(validation_function: Callable) -> Callable:
    @wraps(validation_function)
    def wrapper(*args):
        continue_loop = False
        while continue_loop:
            ...
        return validation_function(*args)
    return wrapper


@infinite_try
def confirm_data(
    data: tuple[str,...],
    confirm_status: str,
    )-> None:
    
    logger.info("Informações de contato: ")
    logger.info(data)
    logger.info("Deseja Confirmar ? [Y/n]")

    confirm_status = confirm_status.upper()

    if not isinstance(confirm_status, str):
        raise ValueError("Por favor, insira um valor válido!")

    if not confirm_status.strip():
        confirm_status = "Y"

    if confirm_status not in ["Y","N"]:
        raise ValueError("Por favor, insira 'y' para confirmar e 'n' para negar")
    
    if confirm_status == "Y":
        logger.info("As informações foram confirmadas!")
        return data
    
    if confirm_status == "N":
        return None
    