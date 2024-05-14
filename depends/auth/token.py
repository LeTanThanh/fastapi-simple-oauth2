from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer

from typing import Annotated

from models.user import UserInDb

from crud.user.get_user import get_user_by_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserInDb:
  user = get_user_by_token(token = token)

  if not user:
    raise HTTPException(
      status_code = status.HTTP_401_UNAUTHORIZED,
      detail = "Invalid authentication credentials",
      headers = {"WWW-Authenticate": "Bearer"}
    )

  return user

async def get_active_current_user(current_user: Annotated[UserInDb, Depends(get_current_user)]):
  if current_user.disabled:
    raise HTTPException(
      status_code = status.HTTP_401_UNAUTHORIZED,
      detail = "Inactive user"
    )

  return current_user
