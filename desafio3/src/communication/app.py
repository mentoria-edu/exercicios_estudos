from flask import Flask, jsonify, request, redirect, url_for
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel


data_test = {"id": 1, "name": "John Doe", "phone": 9878997, "email":"email@exemplo"}

app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Agenda', version="v1.0", servers="http://localhost:8080/proxy/5000/apidoc/openapi.json")


class Contact(BaseModel):
    id : int
    name : str
    phone : int
    email : str


@app.route("/", methods=["GET"])
def show_swagger():
    return redirect('http://localhost:8080/proxy/5000/apidoc/swagger')


@app.route("/contact", methods=["GET"])
def show_contact():
    return jsonify(data_test)


@app.route("/adding_contact", methods=["POST"])
@spec.validate(body=Request(Contact), resp=Response(HTTP_200=Contact))
def adding_contact():
    """Insere uma pessoa na agenda"""
    "função do sqlite insert -(body)"
    return body


@app.route("/viewing_contacts", methods=["GET"])
@spec.validate(resp=Response(HTTP_200=Contact))
def viewing_contacts():
    """retorna todos os contatos da agenda"""
    return "função do sqlite 'quary' para trazer todos os contatos"


@app.route("/contact/<string:name>", methods=["GET"])
@spec.validate(body=Request(Contact), resp=Response(HTTP_200=Contact))
def searching_contact(name):
    """retorna um contato selecionado pelo usuario da agenda"""
    "quary sqlite update usando body e name do banco == name)"
    return jsonify(data_test)


@app.route("/update_contact/<string:name>", methods=["PATCH"])
@spec.validate(body=Request(Contact), resp=Response(HTTP_200=Contact))
def update_contact():
    """quary para alterar contato selecionado pelo usuario da agenda"""
    return


@app.route("/deleting_contact/<string:name>", methods=["DELETE"])
@spec.validate(resp=Response(HTTP_200=Contact))
def deleting_contact():
    """quary para deletar contato selecionado pelo usuario da agenda"""
    return


spec.register(app)

@app.route("/docs/openapi.json")
def serve_openapi():
    return jsonify(spec.spec.to_dict())


if __name__ == "__main__":
    app.run(debug=True)
