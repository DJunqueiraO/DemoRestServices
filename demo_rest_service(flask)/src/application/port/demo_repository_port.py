from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entity.demo import Demo


class DemoRepositoryPort(ABC):

    @abstractmethod
    def find_all(self) -> list[Demo]:
        ...

    @abstractmethod
    def find_by_id(self, id_: int) -> Optional[Demo]:
        ...

    @abstractmethod
    def save(self, demo: Demo) -> Demo:
        ...

    def update(self, demo: Demo) -> Demo:
        ...

    @abstractmethod
    def delete_by_id(self, id_: int) -> bool:
        ...