

def insert_name() -> str:
    name = input("Nome: ")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Insira apenas letras.")
    return name
