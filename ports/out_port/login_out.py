from abc import ABC, abstractmethod


class LoginReadOutPort(ABC):
    @abstractmethod
    async def login(self, username: str, password: str) -> dict:
        pass
