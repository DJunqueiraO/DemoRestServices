from typing import Optional

from src.application.port.test_repository_port import TestRepositoryPort
from src.domain.entity.test import Test


class TestService:
    def __init__(self, repository: TestRepositoryPort):
        self._repository = repository

    def find_all(self) -> list[Test]:
        return self._repository.find_all()

    def find_by_id(self, id_: int) -> Optional[Test]:
        return self._repository.find_by_id(id_)

    def save(self, test: Test) -> Test:
        return self._repository.save(test)

    def update(self, test: Test) -> Test:
        return self._repository.update(test)

    def delete_by_id(self, id_: int) -> bool:
        return self._repository.delete_by_id(id_)