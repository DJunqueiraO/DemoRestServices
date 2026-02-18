from typing import Optional

from typing_extensions import TypeVar, Generic

E = TypeVar("E")
P = TypeVar("P")

class Service(Generic[E, P]):
    def __init__(self, repository: P):
        self._repository = repository

    def find_all(self) -> list[E]:
        return self._repository.find_all()

    def find_by_id(self, id_: int) -> Optional[E]:
        return self._repository.find_by_id(id_)

    def save(self, demo: E) -> E:
        return self._repository.save(demo)

    def update(self, demo: E) -> E:
        return self._repository.update(demo)

    def delete_by_id(self, id_: int) -> bool:
        return self._repository.delete_by_id(id_)