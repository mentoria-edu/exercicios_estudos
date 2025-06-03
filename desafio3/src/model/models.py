import sqlite3
from typing import Any, Optional

DEFAULT_DB_NAME = "model.db"
INIT_DB_FILE = "src/model/sql/init_tables.sql"

def open_sql_script_file(file: str) -> str:
    '''
    
    '''
    with open(file, 'r') as sql_script_file:
        return sql_script_file.read()
    

def execute_query(
        query: str,
        db_name: str = DEFAULT_DB_NAME,
        parameters: tuple[Any, ...] = ()
    ) -> None:
    
    with sqlite3.connect(db_name) as connector: 
        cursor = connector.cursor()
        result = cursor.execute(query, parameters)
        connector.commit()
        return result


def init_db(db_name: str = INIT_DB_FILE) -> None:
    '''

    '''
    execute_query(query=open_sql_script_file(db_name))

def insert_data(data: tuple[str,str,str], db_name: str = DEFAULT_DB_NAME) -> None:
    '''
    
    '''
    query = "INSERT INTO Agenda (`name`, tel_number, email) VALUES (?, ?, ?)"
    execute_query(query=query, db_name=db_name, parameters=data)

def read_data(db_name: str = DEFAULT_DB_NAME) -> tuple:
    '''
    
    '''
    query = "SELECT * FROM Agenda"
    result = execute_query(query=query, db_name=db_name)
    return result

def update_data(id:int, field: str, new_value: str, db_name: str = DEFAULT_DB_NAME) -> None:
    '''
    
    '''
    query = f"UPDATE Agenda SET {field} = ? WHERE id = ?"
    execute_query(query=query, db_name=db_name, parameters=(new_value, id))

def delete_data(id:int, db_name: str = DEFAULT_DB_NAME) -> None:
    '''
    
    '''
    query = f"DELETE FROM Agenda WHERE id = {id}"
    execute_query(query=query, db_name=db_name)