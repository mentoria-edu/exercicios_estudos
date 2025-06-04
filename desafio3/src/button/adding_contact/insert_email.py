import re


def insert_email() -> str:
    regex = r'^[A-Za-z0-9._]+@(?:[a-zA-Z0-9-]+\.){1,2}[A-Za-z]{2,7}$'

    email = input("E-mail: ")
    if not email:  
        raise ValueError("O e-mail não pode estar vazio!")

    if not re.fullmatch(regex, email):
        raise ValueError("Insira um e-mail válido!")

    return email
