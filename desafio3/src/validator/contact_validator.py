import streamlit as st
from .validator import infinite_try
import re
from utils import logger


def validate_name(name: str):

    name = name.strip()

    if not name:
        st.error("O nome não pode estar em branco")

    if len(name) > 100:
        st.error("o nome não pode conter mais que 100 caracteres")

    logger.debug(name)

    return name


def get_valid_phone():
    area_code = _get_valid_area_code()
    phone_number = _get_valid_phone_number()

    final_phone_number = (f"({area_code.strip()}) {phone_number.strip()}")

    logger.debug(final_phone_number)

    return final_phone_number


def _get_valid_area_code(area_code: str) -> str:

    if not area_code.strip():
        st.error("O código de área não pode estar em branco")

    if not area_code.isdigit():
        st.error("O código de área deve conter apenas números")

    if len(area_code) != 2:
        st.error("O código de área deve ter 2 dígitos.")

    return area_code


@infinite_try
def _get_valid_phone_number() -> str:     
    phone_number=input("Digite o número de telefone: ")

    if not phone_number.strip():
        raise ValueError("O número de telefone não pode estar em branco")

    if not phone_number.isdigit():
        raise ValueError("O número de telefone deve conter apenas números")
    
    if len(phone_number) not in [8, 9]:
        raise ValueError("O número de telefone deve ter entre oito e nove dígitos.")
    
    return phone_number


@infinite_try
def get_valid_email()-> str:
    regex = r'^[A-Za-z0-9._-]+@(?:[a-zA-Z0-9-]+\.){1,2}[A-Za-z]{2,7}$'

    email = input("E-mail: ")
    if not email:  
        raise ValueError("O e-mail não pode estar vazio!")

    if not re.fullmatch(regex, email):
        raise ValueError("Insira um e-mail válido!")
    
    return email
     