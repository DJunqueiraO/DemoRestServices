from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entity.test import Test


class TestRepositoryPort(ABC):

    @abstractmethod
    def find_all(self) -> list[Test]:
        ...

    @abstractmethod
    def find_by_id(self, id_: int) -> Optional[Test]:
        ...

    @abstractmethod
    def save(self, test: Test) -> Test:
        ...

    @abstractmethod
    def delete_by_id(self, id_: int) -> bool:
        ...