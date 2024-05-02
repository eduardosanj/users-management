from typing import Optional

from pydantic import BaseModel, EmailStr, Field, constr, conint, create_model


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