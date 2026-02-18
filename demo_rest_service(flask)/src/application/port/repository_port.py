from abc import abstractmethod
from typing import Optional, TypeVar

from typing_extensions import Generic

T = TypeVar("T")

class RepositoryPort(Generic[T]):

    @abstractmethod
    def find_all(self) -> list:
        ...

    @abstractmethod
    def find_by_id(self, id_: int) -> Optional[T]:
        ...

    @abstractmethod
    def save(self, t: T) -> T:
        ...

    def update(self, t: T) -> T:
        ...

    @abstractmethod
    def delete_by_id(self, id_: int) -> bool:
        ...