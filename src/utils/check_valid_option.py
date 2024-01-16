from display_options import list_of_options

def check_valid_option(selected_option):
  does_option_exists = False

  for item in list_of_options:
    current_option = item['option']
    if current_option == selected_option:
      does_option_exists = True
      break
  print("\nSelecione uma opção válida\n")
  return does_option_exists