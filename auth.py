import os

def validate_credentials(username: str, password: str) -> bool:
  correct_username: str = os.environ.get("USERNAME")
  correct_password: str = os.environ.get("PASSWORD")

  correct : bool = True if correct_username == username and correct_password == password else False
  return correct
