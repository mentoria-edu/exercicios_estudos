import sqlite3
import logging


DEFAULT_DB_NAME = "model.db"
DEFAULT_INITIALIZE_SCRIPT = "src/model/sql/book.sql"
DEFAULT_TABLE_NAME="book"
DEFAULT_FIELD_ID_NAME="contact_id"


def execute_sql_script(
    db_name: str = DEFAULT_DB_NAME,
    path_sql_script: str = DEFAULT_INITIALIZE_SCRIPT,
    parameters: tuple[str,...] = ()
) -> None:
    '''
    Execute a sql script 

    Parameters
    ----------
    - `db_name`: String containing the name of the database to connect
    - `path`: The path contains a sql script file

    Returns
    -------
    - None
    '''
    _execute_query(
        query=_open_sql_script_file(path_sql_script),
        db_name=db_name,
        parameters=parameters
    )


def _open_sql_script_file(file_path: str) -> str:
    '''
    Open a sql file and return its contents as a string

    Parameters
    ----------
    - `file`: Path to the file containg the SQL script
  
    Returns
    -------
    - `sql_script_file`: The contents of the SQL script file
    ''' 
    with open(file_path, 'r') as sql_script_file:
        return sql_script_file.read()


def insert_database_row(
    data: tuple[str,...],
    columns_name: tuple[str,...],
    db_name: str = DEFAULT_DB_NAME, 
    table_name: str = DEFAULT_TABLE_NAME,
) -> None:
    '''
    Inserts a row into a specific table using two tuples. 
    The `data` tuple must contain the data that will be 
    inserted into the database.
    The `columns_name` tuple must contain the name of columns
    of the data that will be inserted into the database.


    Parameters
    ----------
    - `data`: Tuple containing data to be included in the table
    - `columns_name`: Tuple containg the name of columns that
    will be insert in the table 
    - `db_name`: String containing the name of the database to connect
    - `table_name`: String containg the name of table

    Returns
    -------
    - None
    '''
    placeholder = _placeholder_template(columns_name)
    columns_name = _join_tuple_values_to_string(columns_name)

    query = f"INSERT INTO {table_name} ({columns_name}) VALUES ({placeholder})"
    _execute_query(query=query, db_name=db_name, parameters=data)


def _placeholder_template(columns_name: tuple[str,...])-> str:
    '''
    Creates a placeholder based on the number of columns passed to the 
    `columns_name` parameter

    Parameters
    ----------
    - `columns_name`: Tuple containg the name of columns that
    will be insert in the table

    Returns
    -------
    - `placeholder`: String contaings a formatted placeholder
    '''
    qtd_of_columns = len(columns_name)
    placeholder_character = "?"
    separetor_character = ","
    
    placeholder_without_separetors = placeholder_character*qtd_of_columns
    placeholder = separetor_character.join(placeholder_without_separetors)
    return placeholder


def _join_tuple_values_to_string(data_tuple: tuple[str,...], sep:str = ","):
    '''
    Transform values in a tuple into a single string using a separator.

    Parameters
    ----------
    - `data_tuple`: Tuple containing the values to be transformed into a string.
    - `sep`: String to be used between the values in the final string.

    Returns
    -------
    - `string_from_tuple`: A single string containing all values from the tuple, 
    separated by the specified separator.
    '''
    string_from_tuple = sep.join(data_tuple)
    return string_from_tuple


def search_rows_by_column(
    field: str,
    value: str,
    db_name: str = DEFAULT_DB_NAME, 
    table_name: str = DEFAULT_TABLE_NAME,
) -> tuple [str,...]:
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
    query = f"SELECT * FROM {table_name} WHERE ({field} LIKE '%' || ? || '%')"
    result = _execute_query(
        query=query,
        db_name=db_name,
        parameters=(value,)
    )
    _show_query_result(result)
    return result


def read_all_data(
    db_name: str = DEFAULT_DB_NAME,
    table_name: str = DEFAULT_TABLE_NAME
) -> tuple:
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
    _show_query_result(result)

    return result


def _show_query_result(query_result: tuple[str,...]):
    '''
    Shows all values from a tuple originating from a database query

    Parameters
    ----------
    - `query_result`: Tuple containing the result of a database query

    Returns
    -------
    - `None`
    '''
    for row in query_result:
        print(row)


def update_column_by_id(
    id:int, 
    field: str,
    new_value: str,
    field_id_name: str = DEFAULT_FIELD_ID_NAME,
    db_name: str = DEFAULT_DB_NAME, 
    table_name: str = DEFAULT_TABLE_NAME
) -> None:
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
    query = f"UPDATE {table_name} SET {field} = ? WHERE {field_id_name} = ? "
    _execute_query(query=query, db_name=db_name, parameters=(new_value, id))


def delete_row_by_id(
        id:int,
        field_id_name: str = DEFAULT_FIELD_ID_NAME, 
        db_name: str = DEFAULT_DB_NAME,
        table_name: str = DEFAULT_TABLE_NAME
) -> None:
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
    query = f"DELETE FROM {table_name} WHERE {field_id_name} = ?"
    _execute_query(query=query, parameters=(id,))


def _execute_query(
    query: str,
    db_name: str = DEFAULT_DB_NAME,
    parameters: tuple[str, ...] = ()
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

    with sqlite3.connect(db_name) as connector: 
        cursor = connector.cursor()
        result = cursor.execute(query, parameters)
        connector.commit()
        logging.info("Operation Success")
        logging.debug(f"Query: {query}")
        logging.debug(f"Parameters: {parameters}")
        return result
