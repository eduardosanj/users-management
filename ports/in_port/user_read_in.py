from abc import ABC, abstractmethod

# Puerto de entrada
class UserReadInPort(ABC):
    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id: str):
        pass