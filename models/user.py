from pydantic import BaseModel

class BaseUser(BaseModel):
  username: str
  email: str | None
  full_name: str | None
  disabled: bool | None

class UserInDb(BaseUser):
  hashed_password: str
