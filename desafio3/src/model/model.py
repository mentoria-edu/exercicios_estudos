import sqlite3
from utils import logger
from collections import namedtuple
from typing import Any

DEFAULT_DB_NAME = "model.db"
TABLE_BOOK_INITIALIZE_SCRIPT = "src/model/sql/book.sql"
DEFAULT_TABLE_NAME = "book"
DEFAULT_FIELD_ID_NAME = "contact_id"
DEFAULT_COLUMNS_NAME = ("name", "phone_number", "email")


def create_book_table(connector: sqlite3.Connection):
    """Creates the book table in the database.
    
    Args:
        connector: SQLite database connection object.
    
    Returns:
        None
    """
    execute_sql_script(
        connector=connector,
        path_sql_script=TABLE_BOOK_INITIALIZE_SCRIPT
    )


def execute_sql_script(
    connector: sqlite3.Connection,
    path_sql_script: str
) -> None:
    """Execute a sql script.

    Args:
        connector: SQLite database connection object.
        path_sql_script: The path contains a sql script file.

    Returns:
        None
    """
    _write_database(
        connector=connector,
        query=_open_sql_script_file(path_sql_script)
    )


def _open_sql_script_file(file_path: str) -> str:
    """Open a sql file and return its contents as a string.

    Args:
        file_path: Path to the file containg the SQL script.
  
    Returns:
        The contents of the SQL script file.
    """
    with open(file_path, 'r') as sql_script_file:
        return sql_script_file.read()


def insert_database_row(
    connector: sqlite3.Connection,
    data: tuple[str, ...],
    table_name: str = DEFAULT_TABLE_NAME,
) -> None:
    """Inserts a row into a specific table using two tuples.
    
    The `data` tuple must contain the data that will be 
    inserted into the database.
    The `columns_name` tuple must contain the name of columns
    of the data that will be inserted into the database.

    Args:
        connector: SQLite database connection object.
        data: Tuple containing data to be included in the table.
        table_name: String containg the name of table.

    Returns:
        None
    """
    columns_name = _get_columns_name(connector, table_name)
    placeholder = _placeholder_template(columns_name)
    columns_name = _join_tuple_values_to_string(columns_name)

    query = f"INSERT INTO {table_name} ({columns_name}) VALUES ({placeholder})"
    _write_database(connector=connector, query=query, parameters=data)


def _placeholder_template(columns_name: tuple[str, ...]) -> str:
    """Creates a placeholder based on the number of columns passed to the 
    `columns_name` parameter.

    Args:
        columns_name: Tuple containg the name of columns that
            will be insert in the table.

    Returns:
        String contaings a formatted placeholder.
    """
    qtd_of_columns = len(columns_name)
    placeholder_character = "?"
    separetor_character = ","
    
    placeholder_without_separetors = placeholder_character * qtd_of_columns
    placeholder = separetor_character.join(placeholder_without_separetors)
    return placeholder


def _get_columns_name(
        connector: sqlite3.Connection,
        table_name: str
    ) -> list[str]:
    """Get column names from a table.

    Args:
        connector: SQLite database connection object.
        table_name: String containg the name of table.

    Returns:
        List of column names.
    """
    cursor = connector.cursor()
    cursor.execute(f'PRAGMA table_info({table_name})')
    columns_name = (*[info[1] for info in cursor.fetchall() if not info[5]],)
    return columns_name


def _join_tuple_values_to_string(data_tuple: tuple[str, ...], sep: str = ","):
    """Transform values in a tuple into a single string using a separator.

    Args:
        data_tuple: Tuple containing the values to be transformed into a string.
        sep: String to be used between the values in the final string.

    Returns:
        A single string containing all values from the tuple, 
        separated by the specified separator.
    """
    string_from_tuple = sep.join(data_tuple)
    return string_from_tuple


def search_rows_by_column(
    connector: sqlite3.Connection,
    field: str,
    value: str,
    table_name: str = DEFAULT_TABLE_NAME,
) -> dict[str:Any]:
    """Performs a query using the LIKE operator with placeholders .

    Args:
        connector: SQLite database connection object.
        field: String containing the name of the field to search.
        value: String containing the value to search for.
        table_name: String containg the name of table.

    Returns:
        Dict containing all matching rows from the database query.
    """
    query = f"SELECT * FROM {table_name} WHERE ({field} LIKE '%' || ? || '%')"
    result = _read_database(
        connector=connector,
        query=query,
        parameters=(value,)
    )
    return result


def read_all_data(
    connector: sqlite3.Connection,
    table_name: str = DEFAULT_TABLE_NAME
) -> dict[str: Any]:
    """Read all data into a specific table.

    Args:
        connector: SQLite database connection object.
        table_name: String containg the name of table.

    Returns:
        Dict containing all the values in a table.
    """
    query = f"SELECT * FROM {table_name}"
    result = _read_database(
        connector=connector,
        query=query, 
    )
    return result


def show_query_result(query_result: dict[str: str] | tuple[str, ...]):
    """Shows all values from a tuple originating from a database query.

    Args:
        query_result: Tuple containing the result of a database query.

    Returns:
        None
    """
    for row in query_result:
        logger.debug(f"Tipo do sub-item: {type(row)}")
        logger.debug(f"Tamanho do sub-item: {len(row)}")
        logger.info(row)


def update_column_by_id(
    connector: sqlite3.Connection,
    id: int, 
    field: str,
    new_value: str,
    field_id_name: str = DEFAULT_FIELD_ID_NAME,
    table_name: str = DEFAULT_TABLE_NAME
) -> None:
    """Updates value from a specific table.

    Args:
        connector: SQLite database connection object.
        id: Int value of the line to be updated.
        field: String containing the name of the column to be updated.
        new_value: String containing the new value to be set.
        field_id_name: String containing the name of the ID field.
        table_name: String containg the name of table.

    Returns:
        None
    """
    query = f"UPDATE {table_name} SET {field} = ? WHERE {field_id_name} = ? "
    _write_database(
        connector=connector, 
        query=query, 
        parameters=(new_value, id)
    )


def delete_row_by_id(
        connector: sqlite3.Connection,
        id: int,
        field_id_name: str = DEFAULT_FIELD_ID_NAME, 
        table_name: str = DEFAULT_TABLE_NAME
) -> None:
    """Delete a row from a specific table.

    Args:
        connector: SQLite database connection object.
        id: Int value of the row to be deleted.
        field_id_name: String containing the name of the ID field.
        table_name: String containg the name of table.

    Returns:
        None
    """
    query = f"DELETE FROM {table_name} WHERE {field_id_name} = ?"
    _write_database(connector=connector, query=query, parameters=(id,))


def _read_database(
        connector: sqlite3.Connection,
        query: str,
        parameters: tuple[str, ...] = ()
    ) -> dict[str: Any]:
    """Read data from database.

    Args:
        connector: SQLite database connection object.
        query: String containing the SQL query.
        parameters: Tuple containing query parameters.

    Returns:
        Dictionary containing the query results.
    """
    connector.row_factory = _dict_factory
    cursor = connector.cursor()
    cursor = cursor.execute(query, parameters)
    rows = cursor.fetchall()
    return rows


def _write_database( 
        connector: sqlite3.Connection,
        query: str,
        parameters: tuple[str, ...] = ()
    ):
    """Write data to database.

    Args:
        connector: SQLite database connection object.
        query: String containing the SQL query.
        parameters: Tuple containing query parameters.

    Returns:
        The result of the query execution.
    """
    cursor = connector.cursor()
    result = cursor.execute(query, parameters)
    connector.commit()
    return result


def _namedtuple_factory(cursor: sqlite3.Cursor, row: str):
    """Transforms an SQLite cursor row into a namedtuple.

    This function is based on the official SQLite documentation.
    For more information, see:
    https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories

    Args:
        cursor: SQLite cursor object.
        row: String representing a database row.

    Returns:
        A namedtuple representing the row.
    """
    fields = [column[0] for column in cursor.description]
    cls = namedtuple("Row", fields)
    return cls._make(row)


def _dict_factory(cursor: sqlite3.Cursor, row: str):
    """Transforms an SQLite cursor row into a dictionary.

    This function is based on the official SQLite documentation.
    For more information, see:
    https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories

    Args:
        cursor: SQLite cursor object.
        row: Database row data.

    Returns:
        A dictionary representing the row.
    """
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}