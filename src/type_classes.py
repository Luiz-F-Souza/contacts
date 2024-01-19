from typing import TypedDict

class Contact(TypedDict):
  name: str
  phone: str
  email: str
  is_favorite: bool
  is_blocked: bool

