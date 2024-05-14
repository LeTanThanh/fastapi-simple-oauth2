from crud.user.all import USER_DBS

from models.user import UserInDb

from utils.password import hash_password
from utils.password import verify_password

def get_user_by_token(token: str) -> UserInDb:
  if token not in USER_DBS:
    return None

  dict_user = USER_DBS[token]
  return UserInDb(**dict_user)

def get_user_by_username_and_password(username: str, password: str) -> UserInDb:
  if username not in USER_DBS:
    return None

  dict_user = USER_DBS[username]
  user = UserInDb(**dict_user)

  if not verify_password(user = user, password = password):
    return None

  return UserInDb(**dict_user)
