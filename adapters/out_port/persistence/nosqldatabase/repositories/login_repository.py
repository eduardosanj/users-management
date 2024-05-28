from bson.objectid import ObjectId
from adapters.out_port.persistence.nosqldatabase.infrastructure.db.database import user_collection
from ports.out_port.login_out import LoginReadOutPort
from typing import List, Optional
from utils.user_helper import user_helper


class LoginRepository(LoginReadOutPort):
    def __init__(self):
        self.collection = user_collection

    async def login(self, username: str, password: str):
        user = await self.collection.find_one({"username": username, "password": password})
        if user:
            return user_helper(user)
        return None
