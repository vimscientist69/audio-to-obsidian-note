import os
import random
import string

def validate_credentials(username: str, password: str) -> bool:
  correct_username: str = os.environ.get("USERNAME")
  correct_password: str = os.environ.get("PASSWORD")

  correct : bool = True if correct_username == username and correct_password == password else False
  return correct

def generate_token() -> str:
  token_len = 20
  return ''.join(random.choices(string.ascii_uppercase + string.digits, k=token_len))
