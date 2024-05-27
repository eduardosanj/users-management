from pydantic import BaseModel

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