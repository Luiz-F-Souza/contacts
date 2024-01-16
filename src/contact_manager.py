from display_options import display_options_list
from add_contact import add_contact
from utils.handle_convert_int import handle_convert_int
from utils.check_valid_option import check_valid_option



def start():

    while True:
        display_options_list()
        selected_option = handle_convert_int(input("Digite uma opção:"))

        if selected_option == None:
            continue

        # is_valid_option = check_valid_option(selected_option)

        # if is_valid_option == False:
        #     continue

        if selected_option == 0:

            continue

        if selected_option == 1:

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

        if selected_option == 3:

            continue

        if selected_option == 4:

            continue

        if selected_option == 5:

            continue

        if selected_option == 6:

            continue
        if selected_option == 9:
            break

    print("Programa finalizado com sucesso")


start()
