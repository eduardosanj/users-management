# from pydantic import BaseModel, constr, Field, conint, EmailStr
# from pydantic.dataclasses import Optional

from typing import Optional
from pydantic import BaseModel, EmailStr, Field, constr, conint


class SchemaDeUser(BaseModel):
    name: constr(strict=True) = Field(...)
    surname: constr(strict=True) = Field(...)
    uid: conint(strict=True, gt=0) = Field(...)
    email: EmailStr = Field(...)
    phone: constr(strict=True) = Field()
    user_type: bool = Field()

    class config:
        schema_extra = {
            "sample": {
                "name": "Juana",
                "surname": "Pilo",
                "uid": 27358783,
                "email": "jpilo@x.ar",
                "phone": "+54 9 456789",
                "user_type": True,
            }
        }


class UpdateUserModel(BaseModel):
    name: Optional[constr(strict=True)]
    surname: Optional[constr(strict=True)]
    uid: Optional[conint(strict=True, gt=0)]
    email: Optional[EmailStr]
    phone: Optional[constr(strict=True)]
    user_type: Optional[bool]

    class Config:
        schema_extra = {
            "sample": {
                "name": "Juana",
                "surname": "Pilo",
                "uid": 27358783,
                "email": "jpilo@x.ar",
                "phone": "+54 9 456789",
                "user_type": True,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}