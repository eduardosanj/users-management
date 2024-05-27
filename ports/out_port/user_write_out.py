from core.domain.user_model import UpdateUserModel, abstractmethod

class UserWriteOutPort(UpdateUserModel):
    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete_by_id(self, id: str):
        pass