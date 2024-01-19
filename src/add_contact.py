from type_classes import Contact
from typing import TypedDict, List
from json import dump, load
from CONTANTS import path_to_db
from utils.get_data import get_data

class AddContactParams(TypedDict):
  name: str
  phone: str
  email: str
  is_favorite: bool

def add_contact(params:AddContactParams):

  new_contact: Contact  = {
    "name": params['name'],
    "phone": params['phone'],
    "email": params["email"],
    "is_favorite": params["is_favorite"],
    "is_blocked": False
  }

  
  contacts = get_data()
  contacts.append(new_contact)


  with open(path_to_db, 'w') as outfile:
    dump(contacts, outfile, indent=2)

  

  print(f"\nContato {params['name']} adicionado com sucesso\n")
  return