from utils.handle_convert_int import handle_convert_int
from utils.get_data import get_data
from CONTANTS import path_to_db
from json import dump


def edit_contact():

    contact_order = input("Ordem do contato para editar: ")

    contact_order_as_int = handle_convert_int(contact_order)

    if contact_order_as_int == None:
        print("Digite uma opção válida")
        return

    option_to_edit = handle_convert_int(input(
        "Digite o que deseja atualizar: 0 para tudo; 1 para nome; 2 para celular e 3 para email."))

    if option_to_edit == None:
        print("Oções válidas para edição são: 0 para tudo; 1 para nome; 2 para celular e 3 para email.")
        return

    contacts = get_data()

    index = contact_order_as_int - 1

    should_edit_all = option_to_edit == 0

    if should_edit_all or option_to_edit == 1:
        name = input("Digite o nome para atualizar: ")
        contacts[index]["name"] = name

    if should_edit_all or option_to_edit == 2:
        phone = input("Digite o celular para atualizar: ")
        contacts[index]["phone"] = phone

    if should_edit_all or option_to_edit == 3:
        email = input("Digite o email para atualizar: ")
        contacts[index]["email"] = email

    print("\nContato editado com sucesso.\n")
    with open(path_to_db, "w") as outfile:
        dump(contacts, outfile, indent=2)
    return
