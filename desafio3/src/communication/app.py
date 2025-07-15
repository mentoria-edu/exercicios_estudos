from flask import Flask, jsonify, request, Blueprint
from pydantic import BaseModel
from src.model import execute_sql_script, insert_database_row, search_rows_by_column, read_all_data, update_column_by_id, delete_row_by_id
from typing import Dict, List, Tuple, Any


bp = Blueprint('routes', __name__)

class Contact_body(BaseModel):
    """Data model for contacts

    Attributes:
    id (int): Unique identifier for the contact
    name (str): Contact name
    phone_number (str): Phone number
    email (str): Email address
    """
    id: int
    name: str
    phone_number: str
    email: str

class Book(BaseModel):
    """Response template for contact list

    Attributes:
    contacts (list[Contact_body]): List of contacts
    count_contacts (int): Total number of contacts
    """
    contacts: list[Contact_body]
    count_contacts: int

class New_contact(BaseModel):
    """Template for creating a new contact

    Attributes:
    name (str): Contact name
    phone_number (str): Phone number
    email (str): Email address
    """
    name: str
    phone_number: str
    email: str

@bp.route("/contacts", methods=["GET"])
def show_contact() -> Dict[List[Dict[str, Any]], int]:
    """Gets all contacts from the address book

    Returns:
    JSON: Book object containing list of contacts and count
    Example: {
    "contacts": [
    {"id": 1, "name": "John", ...},
    ...
    ],
    "count_contacts": 5
    }
    """
    contacts = read_all_data()
    book = Book(
        contacts=contacts,
        count_contacts=len(contacts)
    )
    return jsonify(book.model_dump())

@bp.route("/adding_contact", methods=["POST"])
def adding_contact() -> Tuple[Dict[str, str], int]:
    """Adds new contact to the address book

    Request Body (JSON):
    name (str): Contact name
    phone_number (str): Phone number
    email (str): Email address

    Returns:
    JSON: Confirmation message with HTTP status 201
    Example: {'message': 'contact created'}
    """
    data = request.get_json()
    insert_database_row(
        data=(data['name'], data['phone_number'], data['email']),
        columns_name=('name', 'phone_number', 'email')
    )
    return jsonify({'message': 'contact created'}), 201

@bp.route("/contact/<string:name>", methods=["GET"])
def searching_contact(name) -> Tuple[List[Dict[str, Any]], int]:
    """Search contacts by name

    Parameters:
    name (str): Name to be searched (case-sensitive)

    Returns:
    JSON: List of contacts found
    Example: [{"id": 1, "name": "Maria", ...}]
    """
    result = search_rows_by_column(field='name', value=name)
    return jsonify(result)

@bp.route("/update_contact_name/<int:id>/<string:new_value>", methods=["PATCH"])
def update_contact_name(id, new_value) -> Tuple[Dict[str, str], int]:
    """Updates a contact's name

    Parameters:
    id (int): Contact ID
    new_value (str): New name

    Returns:
    JSON: Confirmation message
    Example: {'message': 'updated contact name'}
    """
    update_column_by_id(id=id, field='name', new_value=new_value)
    return jsonify({'message': 'updated contact name'}), 200

@bp.route("/update_contact_phone/<int:id>/<string:new_value>", methods=["PATCH"])
def update_contact_phone(id, new_value) -> Tuple[Dict[str, str], int]:
    """Updates a contact's phone number

    Parameters:
    id (int): Contact ID
    new_value (str): New phone number

    Returns:
    JSON: Confirmation message
    Example: {'message': 'updated contact phone'}
    """
    update_column_by_id(id=id, field='phone', new_value=new_value)
    return jsonify({'message': 'updated contact phone'}), 200

@bp.route("/update_contact_email/<int:id>/<string:new_value>", methods=["PATCH"])
def update_contact_email(id, new_value) -> Tuple[Dict[str, str], int]:
    """Updates a contact's email

    Parameters:
    id (int): Contact ID
    new_value (str): New email address

    Returns:
    JSON: Confirmation message
    Example: {'message': 'updated contact email'}
    """
    update_column_by_id(id=id, field='email', new_value=new_value)
    return jsonify({'message': 'updated contact email'}), 200

@bp.route("/deleting_contact/<int:id>", methods=["DELETE"])
def deleting_contact(id) -> Tuple[Dict[str, str], int]:
    """Removes a contact from the address book

    Parameters:
    id (int): ID of the contact to be removed

    Returns:
    JSON: Confirmation message
    Example: {'message': 'contact deleted'}
    """
    delete_row_by_id(id)
    return jsonify({'message': 'contact deleted'}), 200

def create_app() -> Flask:
    """Factory function to create and configure the Flask application

    Steps:
    1. Create Flask instance
    2. Register the blueprint with the routes
    3. Execute the SQL script to initialize the database

    Returns:
    Flask: Configured application ready to run
    """
    app = Flask(__name__)
    app.register_blueprint(bp)
    execute_sql_script()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
