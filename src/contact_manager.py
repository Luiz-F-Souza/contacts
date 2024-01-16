from display_options import display_options_list
from add_contact import add_contact
from utils.handle_convert_int import handle_convert_int
from display_contacts import display_contacts


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
                "is_favorit": is_favorite
            })

            continue
        # Adicionar Favorito
        if selected_option == 3:
            display_contacts("not-favorite")

            contact_to_fav = handle_convert_int(
                input("Ordem do contato para favoritar: "))

            if contact_to_fav == None:
                print("\nOrdem selecionada não existe\n")
                while True:
                    want_to_try_again = True if handle_convert_int(
                        input("Deseja tentar outra ordem? Digite 1 para sim: ")) == 1 else False

                    if want_to_try_again == False:
                        break
                    contact_to_fav = handle_convert_int(
                        input("Ordem do contato para favoritar: "))
                    
                    if contact_to_fav == None:
                        continue
                    else:
                        break
                    
                print(f"\nContato ordem {contact_to_fav} favoritado")
            continue

        # Editar contato
        if selected_option == 4:

            continue
        # Deletar contato
        if selected_option == 5:

            continue
        # Bloquear contato
        if selected_option == 6:

            continue
        if selected_option == 9:
            break

        print("Digite um número válido dentre as opções")

    print("Programa finalizado com sucesso")


start()
