from ports.in_port.user_write_in import UserWriteInPort
from ports.out_port.user_write_out import UserWriteOutPort
import uuid
from utils.user_helper import user_helper


class UserWriteUseCase(UserWriteInPort):
    def __init__(self, user_write_out_port: UserWriteOutPort):
        self.user_write_out_port = user_write_out_port

    async def create_user(self, user_data: dict):
        user_data["_id"] = str(uuid.uuid4())  # Genera un ID aleatorio
        user = user_helper(user_data)
        return await self.user_write_out_port.create_user(user)

    async def update_user(self, user_id: str, user_data: dict):
        return await self.user_write_out_port.update_user(user_id, user_data)

    async def delete_user(self, user_id: str):
        return await self.user_write_out_port.delete_user(user_id)
