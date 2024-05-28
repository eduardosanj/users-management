
from pydantic import BaseModel, Field, constr


class LoginModel(BaseModel):
    username: constr(strict=True) = Field(...)
    password: constr(strict=True) = Field(...)