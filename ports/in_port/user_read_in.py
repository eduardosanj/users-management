from abc import ABC, abstractmethod


# Puerto de entrada
class UserReadInPort(ABC):
    @abstractmethod
    async def find_all(self):
        pass

    @abstractmethod
    async def find_by_id(self, id: str):
        pass
