from pydantic import BaseModel

# Modelo para las credenciales de usuario
class User(BaseModel):
    username: str
    password: str

# Modelo para el token JWT
class Token(BaseModel):
    access_token: str
    token_type: str