def create_contact() -> tuple[str, str, str]:
    contact_informations = list()
    contact_informations.append(insert_name())
    contact_informations.append(insert_phone())
    contact_informations.append(insert_email())

    print("Contato adicionado!")
    return tuple(contact_informations)
