from typing import Optional

from pydantic import BaseModel, EmailStr, Field, constr, conint, create_model


class UserModel(BaseModel):
    name: constr(strict=True) = Field(...)
    surname: constr(strict=True) = Field(...)
    username: constr(strict=True) = Field(...)
    password: constr(strict=True) = Field(...)
    email: EmailStr = Field(...)
    phone: constr(strict=True) = Field(None)
    user_type: bool = Field(...)

    class config:
        schema_extra = {
            "sample": {
                "name": "Juana",
                "surname": "Pilo",
                "username": "juanpilo",
                "password": "test",
                "email": "jpilo@x.ar",
                "phone": "+54 9 456789",
                "user_type": True,
            }
        }

class UpdateUserModel(BaseModel):
    name: Optional[constr(strict=True)]
    surname: Optional[constr(strict=True)]
    username: Optional[constr(strict=True)]
    password: Optional[constr(strict=True)]
    email: Optional[EmailStr]
    phone: Optional[constr(strict=True)]
    user_type: Optional[bool]

    class Config:
        schema_extra = {
            "sample": {
                "name": "Juana",
                "surname": "Pilo",
                "username": "juanpilo",
                "password": "test",
                "email": "jpilo@x.ar",
                "phone": "+54 9 456789",
                "user_type": True,
            }
        }

    @classmethod
    def as_optional(cls):
        annonations = cls.__fields__
        fields = {
            attribute: (Optional[data_type.type_], None)
            for attribute, data_type in annonations.items()
        }
        OptionalModel = create_model(f"Optional{cls.__name__}", **fields)
        return OptionalModel


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}