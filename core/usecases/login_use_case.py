from ports.in_port.login_in import LoginReadInPort
from ports.out_port.login_out import LoginReadOutPort
from typing import List, Optional


class LoginReadUseCase(LoginReadInPort):
    def __init__(self, login_read_out_port: LoginReadOutPort):
        self.login_read_out_port = login_read_out_port

    async def login(self, username: str, password: str):
        user = await self.login_read_out_port.login(username, password)
        return user
