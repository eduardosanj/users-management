from abc import ABC, abstractmethod
from typing import List, Optional


class UserReadInPort(ABC):
    @abstractmethod
    async def find_all(self) -> List[dict]:
        pass

    @abstractmethod
    async def find_by_id(self, user_id: str) -> Optional[dict]:
        pass
