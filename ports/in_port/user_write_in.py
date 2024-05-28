from abc import ABC, abstractmethod


class UserWriteInPort(ABC):
    @abstractmethod
    async def create_user(self, user_data: dict):
        pass

    @abstractmethod
    async def update_user(self, user_id: str, user_data: dict) -> bool:
        pass

    @abstractmethod
    async def delete_user(self, user_id: str) -> bool:
        pass
