from bson.objectid import ObjectId
from adapters.out_port.persistence.nosqldatabase.infrastructure.db.database import user_collection
from core.domain.user_model import UserModel
from ports.out_port.user_read_out import UserReadOutPort
from ports.out_port.user_write_out import UserWriteOutPort
from typing import List, Optional
from utils.user_helper import user_helper


class UserRepository(UserReadOutPort, UserWriteOutPort):
    def __init__(self):
        self.collection = user_collection

    async def find_all(self) -> List[dict]:
        users = []
        async for user_data in self.collection.find():
            users.append(user_helper(user_data))
        return users

    async def find_by_id(self, user_id: str) -> Optional[dict]:
        user_data = await self.collection.find_one({"_id": ObjectId(user_id)})
        if user_data:
            return user_helper(user_data)
        return None

    async def create_user(self, user: dict) -> dict:
        result = await self.collection.insert_one(user)
        new_user = await self.collection.find_one({"_id": result.inserted_id})
        return user_helper(new_user)

    async def update_user(self, user_id: str, user_data: dict) -> bool:
        # Devuelve falso si el cuerpo del request está vacio
        if len(user_data) < 1:
            return False
        result = await self.collection.find_one({"_id": ObjectId(user_id)})
        if result:
            updated_user = await self.collection.update_one(
                {"_id": ObjectId(user_id)}, {"$set": user_data}
            )
            if updated_user:
                return True
            return False

    # Delete user
    async def delete_user(self, user_id: str) -> bool:
        user = await self.collection.find_one({"_id": ObjectId(user_id)})
        if user:
            await self.collection.delete_one({"_id": ObjectId(user_id)})
            return True
