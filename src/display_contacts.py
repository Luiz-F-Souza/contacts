from typing import Literal
from utils.get_data import get_data

def display_contacts(display: Literal["all", "favorite", "not-favorite", "not-blocked"]):

  contacts = get_data()
  
  contacts_length = contacts.__len__
  
  if contacts_length == 0:
    print("\nParece que você ainda não cadastrou nenhum contato :(\n")
    return
  
  for index, contact in enumerate(contacts):
    current_contact_order = index + 1
    is_favorite = contact["is_favorit"]
    is_blocked = contact["is_blocked"]

    if display == "favorite" and is_favorite == False:
      continue
    
    if display == "not-favorite" and is_favorite == True:
      continue
    
    if display == "not-blocked" and is_blocked == True:
      continue

    print("\n# # # # # #\n")
    
    print(f"ordem: {current_contact_order}")
    print(f"Nome: {contact["name"]}")
    print(f"Phone: {contact["phone"]}")
    print(f"Email: {contact["email"]}")
    if is_favorite:
      print("❤️ Favoritado ❤️")
    elif is_blocked:
      print(f"❌ Contato Bloqueado ❌")

    print("\n# # # # # #\n")

  return