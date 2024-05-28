# helpers
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "surname": user["surname"],
        "username": user.get("username"),
        "password": user.get("password"),
        "email": user["email"],
        "phone": user["phone"],
        "user_type": user["user_type"]
    }