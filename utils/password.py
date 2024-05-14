from models.user import UserInDb

def hash_password(password: str) -> str:
  return f"fakehashed{password}"

def verify_password(user: UserInDb, password: str) -> bool:
  hashed_password = hash_password(password = password)

  return user.hashed_password == hashed_password
