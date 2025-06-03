from src.menu.menu import run_menu
from src.model.models import init_db, insert_data, read_all_data, update_data, delete_data
from faker import Faker

fake = Faker('pt_br')

data = (fake.name(), fake.phone_number(), fake.email())

init_db()
insert_data(data)
update_data(id=9, field='name', new_value="Leonardo7")
delete_data(id=10)
for row in read_all_data():
    print(row)
