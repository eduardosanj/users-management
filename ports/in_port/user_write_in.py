from abc import ABC, abstractmethod

class UserWriteInPort(ABC):
    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete_by_id(self, id: str):
        pass