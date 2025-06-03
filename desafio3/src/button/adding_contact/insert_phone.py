

def insert_phone() -> str:
    area_code = input("Código de área (DDD): ").strip()
    if not area_code.isdigit() or len(area_code) != 2:
        raise ValueError("O código de área deve ter 2 dígitos.")

    phone = input("Telefone: ")
    if not phone.isdigit() or len(phone) != 8:
        raise ValueError("O telefone deve ter oito dígitos.")

    return str(area_code) + str(phone)
