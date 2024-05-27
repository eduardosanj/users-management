from bson.objectid import ObjectId
from adapters.out_port.persistence.nosqldatabase.infrastructure.db.database import user_collection
from adapters.out_port.persistence.nosqldatabase.repositories.user_helper import user_helper


class UserRepository:
    def __init__(self):
        self.collection = user_collection

    # Search all users
    async def find_all(self):
        users = []
        async for user in self.collection.find():
            users.append(user_helper(user))
        return users

    # Search user by id
    async def find_by_id(self, id: str) -> dict:
        user = await self.collection.find_one({"_id": ObjectId(id)})
        if user:
            return user_helper(user)

    # Register a user
    async def register(self, user_data: dict) -> dict:
        user = await self.collection.insert_one(user_data)
        new_user = await self.collection.find_one({"_id": user.inserted_id})
        return user_helper(new_user)

    # Update user by ID
    async def update(self, id: str, data: dict):
        # Devuelve falso si el cuerpo del request está vacio
        if len(data) < 1:
            return False
        user = await self.collection.find_one({"_id": ObjectId(id)})
        if user:
            updated_user = await self.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            if updated_user:
                return True
            return False

    # Delete user
    async def delete_by_id(self, id: str):
        user = await self.collection.find_one({"_id": ObjectId(id)})
        if user:
            await self.collection.delete_one({"_id": ObjectId(id)})
            return True
