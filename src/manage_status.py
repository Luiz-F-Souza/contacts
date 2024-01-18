from typing import List
from utils.get_data import get_data
from json import dump
from utils.handle_convert_int import handle_convert_int
from typing import Literal
from CONTANTS import path_to_db



def manage_status(contacts_input: List[str], type: Literal["block","fav"]):
    contacts = get_data()

    
    for contact in contacts_input:
        order = handle_convert_int(contact)
        if order == None:
            print(f"contato {order} não existe.")
            continue
        index = order - 1
        if index < 0 or index > contacts.__len__():
            print(f"contato {order} fora do range atual")
        current_contact = contacts[index]
        current_contact['is_favorit'] = True if type == 'fav' else False
        current_contact['is_blocked'] = True if type == 'block' else False

    with open(path_to_db, 'w') as outfile:
        dump(contacts, outfile, indent=2)
    return
