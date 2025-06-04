"""buttons package initializer."""

from adding_contact.insert_name import insert_name
from adding_contact.insert_phone import insert_phone
from adding_contact.insert_email import insert_email
from adding_contact.create_contact import create_contact


contact_informations = list()
contact_informations.append(insert_name())
contact_informations.append(insert_phone())
contact_informations.append(insert_email())


tuple(contact_informations)