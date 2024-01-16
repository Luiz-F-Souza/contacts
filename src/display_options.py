from typing import List, TypedDict

class Option(TypedDict):
    name: str
    option: int

list_of_options: List[Option] = [
    {"name": "Ver contatos", "option": 0},
    {"name": "Ver Favoritos", "option": 1},
    {"name": "Adicionar contato", "option": 2},
    {"name": "Adicionar Favorito", "option": 3},
    {"name": "Editar contato", "option": 4},
    {"name": "Deletar contatos", "option": 5},
    {"name": "Bloquear contatos", "option": 6},
    {"name": "Sair", "option": 9},
]


def display_options_list():
    print("\n")
    print("##### Lista de opções #####")

    for current_option in list_of_options:
        print(f"{current_option["name"]}: {current_option["option"]}")

    print("\n")
    return
