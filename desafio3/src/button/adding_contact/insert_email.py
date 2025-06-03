
import re


def insert_email() -> str:
    regex = r'\b[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'

    email = input("E-mail: ")
    if(re.fullmatch(regex, email)):
        return email
    raise ValueError("Insira um e-mail válido.")
