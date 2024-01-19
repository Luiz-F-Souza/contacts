from display_options import display_options_list
from add_contact import add_contact
from manage_status import manage_status
from utils.handle_convert_int import handle_convert_int
from display_contacts import display_contacts
from delete_contact import delete_contacts
from edit_contact import edit_contact


def start():

    while True:
        display_options_list()
        selected_option = handle_convert_int(input("Digite uma opção: "))

        if selected_option == None:
            continue

        # Ver contatos
        if selected_option == 0:
            display_contacts("all")
            continue
        # Ver favoritos
        if selected_option == 1:
            display_contacts("favorite")
            continue

        # ADD Contact
        if selected_option == 2:
            print("\nDigite os dados do contato abaixo\n")
            name_to_register = input("Nome: ")
            phone_to_register = input("Celular: ")
            email_to_register = input("Email: ")
            is_favorite = True if handle_convert_int(
                input("Deseja adicionar aos favoritos? 1 para SIM: ")) == 1 else False

            add_contact({
                "name": name_to_register,
                "phone": phone_to_register,
                "email": email_to_register,
                "is_favorite": is_favorite
            })

            continue
        # Adicionar Favorito
        if selected_option == 3:
            display_contacts("not-favorite")

            print("Digite números separados por espaço para favoritar vários. Ex: 12 32 43 23")
            contacts_to_fav = input("Ordem do contato para favoritar: ")

            contacts_list = list(contacts_to_fav.split(" "))

            manage_status(contacts_list, "fav")
            continue

        # Editar contato
        if selected_option == 4:
            display_contacts("all")

            edit_contact()

            continue

        # Deletar contato
        if selected_option == 5:
            display_contacts("all")

            print("Digite números separados por espaço para DELETAR vários. Ex: 12 32 43 23")
            contacts_to_del = input("Ordem do contato para DELETAR: ")

            delete_contacts(contacts_to_del)
            continue

        # Bloquear contato
        if selected_option == 6:

            display_contacts("not-blocked")

            print("Digite números separados por espaço para favoritar vários. Ex: 12 32 43 23")
            contacts_to_block = input("Ordem do contato para favoritar: ")

            contacts_list = list(contacts_to_block.split(" "))

            manage_status(contacts_list, "block")

            continue
        if selected_option == 9:
            break

        print("Digite um número válido dentre as opções")

    print("Programa finalizado com sucesso")


start()
