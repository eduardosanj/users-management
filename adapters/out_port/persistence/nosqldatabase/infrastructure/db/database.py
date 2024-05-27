import os
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])

database = client.users

user_collection = database.get_collection("users_collections")