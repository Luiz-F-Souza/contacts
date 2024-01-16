def handle_convert_int(string_to_convert):
  try:
    return int(string_to_convert)
  except:
    print("\nDigite um número válido!")
    return None