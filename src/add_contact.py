from typing import TypedDict, List
from json import dump, dumps, load
from pathlib import Path


current_file_path = Path(__file__).parent.resolve()

print(f"current_file_path: {current_file_path}")

class AddContactParams(TypedDict):
  name: str
  phone: str
  email: str
  is_favorit: bool

def add_contact(params:AddContactParams):

  path_to_db = f'{current_file_path}/data/data.json'

  new_contact = {
    "name": params['name'],
    "phone": params['phone'],
    "email": params["email"],
    "is_favorit": params["is_favorit"],
    "is_blocked": False
  }

  with open(path_to_db,'r') as openfile:
    data = list(load(openfile))

  data.append(new_contact)


  with open(path_to_db, 'w') as outfile:
    dump(data, outfile, indent=2)

  



  

  print(f"\nContato {params['name']} adicionado com sucesso\n")
  return