from src.application.port.demo_repository_port import DemoRepositoryPort
from src.application.services.service import Service
from src.domain.entity.demo import Demo


class DemoService(Service[Demo, DemoRepositoryPort]):
    def __init__(self, repository: DemoRepositoryPort):
        super().__init__(repository)