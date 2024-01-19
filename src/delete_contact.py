from typing import List
from utils.get_data import get_data
from utils.handle_convert_int import handle_convert_int
from CONTANTS import path_to_db
from json import dump


def delete_contacts(contacts_to_del: List[str]):

    has_confirmed = True if handle_convert_int(
        input("Tem certeza que deseja apagar ? Digite 1 para sim: ")) == 1 else False

    if has_confirmed == False:
        print("Operação cancelada")
        return

    contacts = get_data()

    for contact_to_del in contacts_to_del:

        contact_order_as_int = handle_convert_int(contact_to_del)

        if contact_order_as_int == None:
            print(f"Digite uma ordem válida, {contact_to_del} não é um número")
            continue

        index = contact_order_as_int - 1
        
        if index < 0 or index > contacts.__len__():
            print(f"Ordem {contact_to_del} não existe")
            continue

        del contacts[index]

    with open(path_to_db, "w") as outfile:
        dump(contacts, outfile, indent=2)

    return
