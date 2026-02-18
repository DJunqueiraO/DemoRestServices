from typing import Optional

from src.application.port.demo_repository_port import DemoRepositoryPort
from src.domain.entity.demo import Demo


class DemoService:
    def __init__(self, repository: DemoRepositoryPort):
        self._repository = repository

    def find_all(self) -> list[Demo]:
        return self._repository.find_all()

    def find_by_id(self, id_: int) -> Optional[Demo]:
        return self._repository.find_by_id(id_)

    def save(self, demo: Demo) -> Demo:
        return self._repository.save(demo)

    def update(self, demo: Demo) -> Demo:
        return self._repository.update(demo)

    def delete_by_id(self, id_: int) -> bool:
        return self._repository.delete_by_id(id_)