def search_for_a_contact():
    search = input("Buscar: ")

    for contact in contact_list:
        if search in contact["nome"]:
            print(f"{contact['nome']} - {contact['telefone']}")
