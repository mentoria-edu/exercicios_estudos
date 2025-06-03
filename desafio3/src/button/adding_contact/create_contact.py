
#1.3
def create_contact():
    name = insert_name()
    phone = insert_phone()
    email = insert_email()


    new_contact = {"nome": name, "telefone": phone, "email": email}
    print("Contato adicionado!")
    return new_contact
