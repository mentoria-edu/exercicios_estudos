from src.model import(
    execute_sql_script,
    insert_database_row,
    search_rows_by_column,
    read_all_data,
    update_column_by_id,
    delete_row_by_id,
)

# from faker import Faker

# fake = Faker('pt_br')
# data = (fake.name(), fake.phone_number(), fake.email())
# colunms_name = ("name","phone_number","email")





# # # print(consulta)
# # # for row in consulta:
# # #     print(row)
# # delete_row_by_id(id=15)
# # update_column_by_id(id=11,field="name",new_value="Leonardo A. Souza")
# # print(f"\nTodos os valores")
# # result = read_all_data()
# # for row in result:
# #     print(row)
# # # update_data(id=9, field='name', new_value="Leonardo7")
# # # delete_data(id=10)

# # # print("\nDepois das mudanças \n")
# # # update_data(id=1, field='name', new_value="Novo Nome")
# # # delete_data(id=2)


# # # for row in read_all_data():
# # #     print(row)

# print("Antes do Update")
# result = read_all_data()
# for row in result:
#     print(row)

# delete_row_by_id(id=12)

# print("Depois do Update")
# result = read_all_data()
# for row in result:
#     print(row)


from src.button import get_contact_informations
import sqlite3

DEFAULT_DB_NAME = "model.db"

colunms_name = ("name","phone_number","email")

# execute_sql_script()
# data = get_contact_informations()

# execute_sql_script()


data = get_contact_informations()
with sqlite3.connect(DEFAULT_DB_NAME) as connector:
    insert_database_row(connector=connector, data=data, columns_name=colunms_name)
    result = read_all_data(connector)