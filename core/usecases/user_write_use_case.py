from ports.in_port.user_write_in import UserWriteInPort
from ports.out_port.user_write_out import UserWriteOutPort

class UserWriteUseCase(UserWriteInPort):    
    def __init__(self, user_write_out_port: UserWriteOutPort):
        self.user_write_out_port = user_write_out_port

    async def register(self):
        return await self.user_write_out_port.register()

    async def update(self, id: str):
        return await self.user_write_out_port.update(id)

    async def delete_by_id(self, id: str):
        return await self.user_write_out_port.delete(id)