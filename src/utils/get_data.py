from CONTANTS import path_to_db
from json import load
from typing import List
from type_classes import Contact

def get_data():
  with open(path_to_db, 'r') as openfile:
    contacts: List[Contact]  = list(load(openfile))
  return contacts
  