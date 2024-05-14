from fastapi import FastAPI
from fastapi import Depends

from typing import Annotated

from models.user import UserInDb

from depends.auth.token import get_active_current_user
from depends.auth.pasword import get_user_by_password_request_form

app = FastAPI()

@app.post("/token")
async def sign_in(user: Annotated[UserInDb, Depends(get_user_by_password_request_form)]):
  return {
    "access_token": user.username,
    "token_type": "bearer"
  }

@app.post("/users/me")
async def read_user_me(current_user: Annotated[str, Depends(get_active_current_user)]) -> UserInDb:
  return current_user
