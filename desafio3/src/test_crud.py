from src.menu.menu import run_menu
from src.model.models import init_db, insert_data, read_data, update_data, delete_data
from faker import Faker

fake = Faker('pt_br')

data = (fake.name(), fake.phone_number(), fake.email())

init_db()
insert_data(data)
insert_data(data)
print("Antes das mudanças \n")
for row in read_data():
    print(row)

print("\nDepois das mudanças \n")
update_data(id=1, field='name', new_value="Novo Nome")
delete_data(id=2)

for row in read_data():
    print(row)