from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response
from pydantic import BaseModel


app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Agenda', version="v1.0", path="/apidoc", servers="http://localhost:8080/proxy/5000/apidoc/openapi.json")

class Contact(BaseModel):
    id: int
    name: str
    phone: int
    email: str

@app.route("/", methods=["GET"])
@spec.validate(resp=Response(HTTP_200=Contact))
def show_menu():
    return jsonify([{"id": 1, "name": "John Doe", "phone": 9878997, "email":"email@exemplo"}])

@app.route("/adding_contact", methods=["POST"])
@spec.validate(resp=Response(HTTP_200=Contact))
def adding_contact():
    return jsonify([{"id": 1, "name": "John Doe", "phone": 9878997, "email":"email@exemplo"}])

@app.route("/viewing_contacts", methods=["GET"])
@spec.validate(resp=Response(HTTP_200=Contact))
def viewing_contacts():
    return jsonify([{"id": 1, "name": "John Doe", "phone": 9878997, "email":"email@exemplo"}])

@app.route("/searching_contact", methods=["GET"])
@spec.validate(resp=Response(HTTP_200=Contact))
def searching_contact():
    return jsonify([{"id": 1, "name": "John Doe", "phone": 9878997, "email":"email@exemplo"}])

@app.route("/update_contact", methods=["PATCH"])
@spec.validate(resp=Response(HTTP_200=Contact))
def update_contact():
    return jsonify([{"id": 1, "name": "John Doe", "phone": 9878997, "email":"email@exemplo"}])

@app.route("/deleting_contact", methods=["DELETE"])
@spec.validate(resp=Response(HTTP_200=Contact))
def deleting_contact():
    return jsonify([{"id": 1, "name": "John Doe", "phone": 9878997, "email":"email@exemplo"}])

spec.register(app)

@app.route("/docs/openapi.json")
def serve_openapi():
    return jsonify(spec.spec.to_dict())


if __name__ == "__main__":
    app.run(debug=true)