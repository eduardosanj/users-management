from ports.in_port.user_read_in import UserReadInPort
from ports.out_port.user_read_out import UserReadOutPort


class UserReadUseCase(UserReadInPort):
    def __init__(self, user_read_out_port: UserReadOutPort):
        self.user_read_out_port = user_read_out_port

    async def find_all(self):
        return await self.user_read_out_port.find_all()

    async def find_by_id(self, id: str):
        return await self.user_read_out_port.find_by_id(id)
