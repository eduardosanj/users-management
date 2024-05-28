import secrets


def generate_jwt_secret_key(length=32):
    return secrets.token_hex(length)
