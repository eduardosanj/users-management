
from pydantic import BaseModel, Field, constr


class UserLoginModel(BaseModel):
    username: constr(strict=True) = Field(...)
    password: constr(strict=True) = Field(...)