import jwt
import datetime
from server.models.token import User
# Clave secreta para firmar el token (debería ser segura y aleatoria en un entorno real)
SECRET_KEY = 'dnVvODY4Yzc2bzhzNzZqOG83czY4b2Nq'

# Función para generar un token JWT
def generate_token(payload: dict):
    # Configurar la información del token (puedes incluir cualquier dato relevante)
    # payload = {
    #     'username': data.username,
    #     'password': data.password,
    #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # Expira en 30 minutos
    # }
    
    # Generar el token JWT firmado con la clave secreta
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Función para verificar un token JWT
def validate_token(token):
    try:
        # Decodificar el token JWT con la clave secreta
        response = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return response  # Devuelve los datos del token si es válido
    except jwt.ExpiredSignatureError:
        return 'The token has expired'  # Manejo de token expirado
    except jwt.InvalidTokenError:
        return 'Invalid token'  # Manejo de token inválido

# # Ejemplo de uso:
payload = {'username': "test", 'password': "test", 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
token_generate = generate_token(payload)
print("Token generate:", token_generate)

verified_data = validate_token(token_generate)
print("Verified Data:", verified_data)
