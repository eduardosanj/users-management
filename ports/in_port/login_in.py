from abc import ABC, abstractmethod


class LoginReadInPort(ABC):
    @abstractmethod
    async def login(self, username: str, password: str) -> dict:
        pass
