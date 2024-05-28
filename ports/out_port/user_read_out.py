from abc import ABC, abstractmethod
from typing import List, Optional
from core.domain.user_model import UserModel


class UserReadOutPort(ABC):
    @abstractmethod
    async def find_all(self) -> List[dict]:
        pass

    @abstractmethod
    async def find_by_id(self, user_id: str) -> Optional[dict]:
        pass
