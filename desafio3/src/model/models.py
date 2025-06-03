import sqlite3
from typing import Any, Optional

DEFAULT_DB_NAME = "model.db"
DEFAULT_INITIALIZE_SCRIPT = "src/model/sql/init_tables.sql"
DEFAULT_TABLE_NAME="Agenda"

def open_sql_script_file(file: str) -> str:
    '''
    Open a sql file and return its contents as a string

    Parameters
    ----------
    - `file`: Path to the file containg the SQL script
  
    Returns
    -------
    - `sql_script_file`: The contents of the SQL script file
    ''' 
    with open(file, 'r') as sql_script_file:
        return sql_script_file.read()
    

def _execute_query(
        query: str,
        db_name: str = DEFAULT_DB_NAME,
        parameters: tuple[Any, ...] = ()
    ) -> str:
    '''
    Try execute a query on a specific database.
    If successful, returns a String containing the result of the query
    If it fails, it returns an error message.

    Parameters
    ----------
    - `query`: String contains an SQL query
    - `db_name`: String containing the name of the database to connect
    - `parameters`: Tuple containing data to be included in a query

    Returns
    -------
    - `result`: String containing the result of the query
    '''
    try:
        with sqlite3.connect(db_name) as connector: 
            cursor = connector.cursor()
            result = cursor.execute(query, parameters)
            connector.commit()
            print("Operação realizada com sucesso!")
            return result
    except Exception as err:
            print(f"Falha na Consulta! \nMotivo do Erro: {str(err)}")


def init_db(
        db_name: str = DEFAULT_DB_NAME, 
        path_sql_script: str = DEFAULT_INITIALIZE_SCRIPT
    ) -> None:
    '''
    Creates an SQLite database if it doesn't exist from an sql script 

    Parameters
    ----------
    - `db_name`: String containing the name of the database to connect
    - `path`: The path contains a sql script file

    Returns
    -------
    - None
    '''
    _execute_query(
        query=open_sql_script_file(path_sql_script),
        db_name=db_name
        )

def insert_data(data: tuple[str,str,str], db_name: str = DEFAULT_DB_NAME, table_name: str = DEFAULT_TABLE_NAME) -> None:
    '''
    Inserts data into a specific table using a tuple

    Parameters
    ----------
    - `data`: Tuple containing data to be included in the table
    - `db_name`: String containing the name of the database to connect
    - `table_name`: String containg the name of table

    Returns
    -------
    - None
    '''
    query = f"INSERT INTO {table_name} (`name`, tel_number, email) VALUES (?, ?, ?)"
    _execute_query(query=query, db_name=db_name, parameters=data)

def read_all_data(db_name: str = DEFAULT_DB_NAME, table_name: str = DEFAULT_TABLE_NAME) -> tuple:
    '''
    Read all data into a specific table

    Parameters
    ----------
    - `db_name`: String containing the name of the database to connect
    - `table_name`: String containg the name of table

    Returns
    -------
    - `result`: Tuple containing all the values in a table
    '''
    query = f"SELECT * FROM {table_name}"
    result = _execute_query(query=query, db_name=db_name)
    return result

def update_data(id:int, field: str, new_value: str, db_name: str = DEFAULT_DB_NAME, table_name: str = DEFAULT_TABLE_NAME) -> None:
    '''
    Updates value from a specific table 

    Parameters
    ----------
    - `id`: Int value of the line to be updated
    - `field`: String containing the name of the column to be updated
    - `db_name`: String containing the name of the database to connect
    - `table_name`: String containg the name of table

    Returns
    -------
    - None
    '''
    query = f"UPDATE {table_name} SET {field} = ? WHERE id = ?"
    _execute_query(query=query, db_name=db_name, parameters=(new_value, id))

def delete_data(id:int, db_name: str = DEFAULT_DB_NAME, table_name: str = DEFAULT_TABLE_NAME) -> None:
    '''
    Delete a row from a specific table 

    Parameters
    ----------
    - `id`: Int value of the row to be deleted
    - `db_name`: String containing the name of the database to connect
    - `table_name`: String containg the name of table

    Returns
    -------
    - None
    '''
    query = f"DELETE FROM {table_name} WHERE id = {id}"
    _execute_query(query=query, db_name=db_name)