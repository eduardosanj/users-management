from pydantic import BaseModel

# Modelo para las credenciales de usuario
class User(BaseModel):
    username: str
    password: str

# Modelo para el token JWT
class Token(BaseModel):
    access_token: str
    token_type: str


def ResponseToken(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
}


def ErrorResponseToken(error, code, message):
    return {"error": error, "code": code, "message": message}