from ports.in_port.user_read_in import UserReadInPort
from ports.out_port.user_read_out import UserReadOutPort
from typing import List, Optional


class UserReadUseCase(UserReadInPort):
    def __init__(self, user_read_out_port: UserReadOutPort):
        self.user_read_out_port = user_read_out_port

    async def find_all(self) -> List[dict]:
        users = await self.user_read_out_port.find_all()
        return [user for user in users]

    async def find_by_id(self, user_id: str) -> Optional[dict]:
        user = await self.user_read_out_port.find_by_id(user_id)
        if user:
            return user
        return None
