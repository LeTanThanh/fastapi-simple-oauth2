from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm

from typing import Annotated

from models.user import UserInDb

from crud.user.get_user import get_user_by_username_and_password

async def get_user_by_password_request_form(form: Annotated[OAuth2PasswordRequestForm, Depends()]) -> UserInDb:
  username = form.username
  password = form.password
  user = get_user_by_username_and_password(username = username, password = password)

  if not user:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail = "Incorrect username or password"
    )

  return user
