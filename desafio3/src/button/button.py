import re


DEFAULT_COLUMNS_NAME = ("name", "phone_number", "email")


def insert_name() -> str:
    name = input("Nome: ")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Insira apenas letras.")
    return name


def insert_phone() -> str:
    area_code = input("Código de área (DDD): ").strip()
    if not area_code.isdigit() or len(area_code) != 2:
        raise ValueError("O código de área deve ter 2 dígitos.")

    phone = input("Telefone: ")
    if not phone.isdigit() or len(phone) != 8:
        raise ValueError("O telefone precisa deve ter oito dígitos.")

    return area_code + phone


def insert_email() -> str:
    regex = r'^[A-Za-z0-9._]+@(?:[a-zA-Z0-9-]+\.){1,2}[A-Za-z]{2,7}$'

    email = input("E-mail: ")
    if not email:  
        raise ValueError("O e-mail não pode estar vazio!")

    if not re.fullmatch(regex, email):
        raise ValueError("Insira um e-mail válido!")

    return email


def get_contact_information() -> tuple[str, str, str]:

    name = insert_name()
    phone_number = insert_phone()
    email = insert_email()

    contact_information = (name, phone_number, email)

    return contact_information

get_contact_information()
